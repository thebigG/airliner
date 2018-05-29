import math
import re
import time
from numbers import Real

from geographic import GeographicBase
from position import Position
from pyliner_module import PylinerModule
from telemetry import SetpointTriplet

_NAV_SLEEP = 1/16


def constant(value):
    return lambda current, target: value


def proportional(const, neutral=0.0):
    return lambda current, target: (target - current) * const + neutral


def limiter(min_val, max_val):
    return lambda val: max(min(val, max_val), min_val)


# TODO Look into using decimal library for precision at any lat/lon


class Waypoint(Position):
    """A container for part of the args to a triplet."""
    def __init__(self, latitude, longitude, altitude, heading):
        super(Waypoint, self).__init__(latitude, longitude, altitude)
        self.heading = heading

    def __repr__(self):
        return '{}({}, {}, {}, {})'.format(
            self.__class__.__name__, self.latitude, self.longitude,
            self.altitude, self.heading)

    @property
    def yaw(self):
        if self.heading is None:
            return None
        return math.radians(self.heading if self.heading < 180
                            else self.heading - 360)


class Navigation(PylinerModule):
    """Navigation module. Contains all navigation features.

    Note:
        Currently this module takes lateral and vertical navigation as separate
        components, and only executes one at a time.
    TODO: In a future version a more integrated 3d-space will be implemented.
    """

    def __init__(self, geographic):
        # type: (GeographicBase) -> None
        super(Navigation, self).__init__()
        self._geographic = geographic
        self._telemetry = None

    req_telem = {
        'latitude': '/Airliner/CNTL/VehicleGlobalPosition/Lat',
        'longitude': '/Airliner/CNTL/VehicleGlobalPosition/Lon',
        'altitude': '/Airliner/CNTL/VehicleGlobalPosition/Alt',
        'yaw': '/Airliner/CNTL/VehicleGlobalPosition/Yaw',
        'velN': '/Airliner/CNTL/VehicleGlobalPosition/VelN',
        'velE': '/Airliner/CNTL/VehicleGlobalPosition/VelE',
        'velD': '/Airliner/CNTL/VehicleGlobalPosition/VelD'
    }

    # Public Navigation Properties
    @property
    def altitude(self):
        """meters"""
        return PylinerModule._telem(self.req_telem['altitude'])(self)

    @property
    def heading(self):
        """Degrees"""
        # TODO add setter for property
        return self.yaw % 360  # mod is for negative degrees.

    @property
    def latitude(self):
        """Degrees"""
        return PylinerModule._telem(self.req_telem['latitude'])(self)

    @property
    def longitude(self):
        """Degrees"""
        return PylinerModule._telem(self.req_telem['longitude'])(self)

    @property
    def position(self):
        """The spatial state of the vehicle."""
        return Waypoint(self.latitude, self.longitude,
                        self.altitude, self.heading)

    @property
    def yaw(self):
        """The vehicle yaw in clockwise radians from north."""
        return math.degrees(PylinerModule._telem(self.req_telem['yaw'])(self))

    def backward(self, distance, method, tolerance=1):
        """Move backward by a distance. See lnav for full documentation."""
        self.lnav(distance, '-x', method, tolerance)

    def clockwise(self, degrees, method, tolerance=1):
        """Rotate clockwise by a number of degrees."""
        old_heading = self.heading
        target_heading = (old_heading + degrees) % 360
        min_tol = (target_heading - tolerance) % 360

        def unroll_heading():
            return self.heading if self.heading < target_heading \
                else self.heading - 360

        while unroll_heading() < min_tol:
            self.vehicle.fd.r = method(unroll_heading(), target_heading)
            time.sleep(_NAV_SLEEP)
        self.vehicle.fd.r = 0.0

    def counterclockwise(self, degrees, method, tolerance=1):
        """Rotate counterclockwise by a number of degrees."""
        old_heading = self.heading
        target_heading = (old_heading - degrees) % 360
        max_tol = (target_heading + tolerance) % 360

        def unroll_heading():
            return self.heading if self.heading > target_heading \
                else self.heading + 360

        while unroll_heading() > max_tol:
            self.vehicle.fd.r = method(unroll_heading(), target_heading)
            time.sleep(_NAV_SLEEP)
        self.vehicle.fd.r = 0.0

    def down(self, distance, method, tolerance=1):
        """Move down by a distance. See vnav for full documentation."""
        self.vnav(by=-distance, method=method, tolerance=tolerance)

    def forward(self, distance, method, tolerance=1):
        """Move forward by a distance. See lnav for full documentation."""
        self.lnav(distance, 'x', method, tolerance)

    def goto(self, waypoint, tolerance=1):
        # type: (Waypoint, Real) -> None
        """Move the vehicle to a waypoint.

        Block until the distance between the waypoint and the vehicle is within
        tolerance.
        """
        self._telemetry = SetpointTriplet(
            Cur_Lat=waypoint.latitude,
            Cur_Lon=waypoint.longitude,
            Cur_Alt=self.altitude if waypoint.altitude is None else waypoint.altitude,
            Cur_Yaw=self.yaw if waypoint.heading is None else waypoint.yaw,
            Cur_Valid=1, Cur_PositionValid=1
        )
        while self._geographic.distance(waypoint, self.position) > tolerance:
            time.sleep(_NAV_SLEEP)

    def left(self, distance, method, tolerance=1):
        """Move left by a distance. See lnav for full documentation."""
        self.lnav(distance, '-y', method, tolerance)

    def lnav(self, distance, axis, method, tolerance):
        """Perform a lateral movement.

        Block until the distance traveled is within the tolerance of the target
        distance.

        Args:
            distance (Real): Distance in meters to move.
            axis (str): Must be one of the lateral movement axes (x, y, or z),
                and may be prefixed by an optional "-" for negative movement.
            method (Callable[[Real, Real], Real]): Callable takes two arguments,
                the distance traveled and the target distance, and returns an
                axis control value within [-1, 1].
            tolerance (Real): The allowable error in movement before the method
                sets the control to 0 and returns.
        """
        axis_match = re.match('(-)?([xyz])', axis)
        if not axis_match:
            raise ValueError('Axis must match "(-)?([xyz])".')
        neg, axis = axis_match.groups()
        original = self.position
        delta = self._geographic.distance(original, self.position)
        while (distance - delta) > tolerance:
            velocity = method(delta, distance)
            setattr(self.vehicle.fd, axis, -velocity if neg else velocity)
            time.sleep(_NAV_SLEEP)
            delta = self._geographic.distance(original, self.position)
        setattr(self.vehicle.fd, axis, 0.0)

    @classmethod
    def required_telemetry_paths(cls):
        return cls.req_telem.values()

    def right(self, distance, method, tolerance=1):
        """Move right by a distance. See lnav for full documentation."""
        self.lnav(distance, 'y', method, tolerance)

    @property
    def telemetry(self):
        t = self._telemetry
        self._telemetry = None
        return t

    @property
    def telemetry_available(self):
        return self._telemetry is not None

    def up(self, distance, method=None, tolerance=1):
        """Move up by a distance. See vnav for full documentation."""
        self.vnav(by=distance, method=method, tolerance=tolerance)

    def vnav(self, by=None, to=None, method=None, tolerance=1):
        """Perform a vertical navigation.

        Blocks until the vehicle altitude is within tolerance of the target
        change or absolute altitude.

        Args:
            by (Real): Change altitude by this amount. May be negative. Cannot
                be set at the same time as `to`.
            to (Real): Ascend or descend to this altitude. Cannot be set at the
                same time as `by`.
            method (Callable[[Real, Real], Real]): Callable takes two arguments,
                the current altitude and the target altitude, and returns an
                axis control value within [-1, 1].
            tolerance (Real): The allowable error in altitude before the method
                sets the z-axis to 0 and returns.
        """
        if not any((by, to)):
            raise ValueError('Must set either by or to.')
        elif by and to:
            raise ValueError('Cannot set both by and to.')
        if not method:
            raise ValueError('Must have navigation method.')
        if not isinstance(tolerance, Real) or tolerance <= 0:
            raise ValueError('Tolerance must be set to a positive real number.')
        target_altitude = (self.altitude + by) if by is not None else to
        while abs(target_altitude - self.altitude) > tolerance:
            self.vehicle.fd.z = method(self.altitude, target_altitude)
            time.sleep(_NAV_SLEEP)
        self.vehicle.fd.z = 0.0
