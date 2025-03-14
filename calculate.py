# calculate.py

import math
import numpy as np

def calculate_positive(data):
    """ 
    data = {
        'world coordinates' : { 'x' : '', 'y' : '', 'z' : '' },
        'fitting func coefs' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'fitting func coefs reverse' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'camera pose' : { 'pitch' : '', 'yaw' : '', 'roll' : '' },
        'sensor params' : { 'width' : '', 'height' : '', 'pixel size' : '' },
        'camera coordinates' : { 'x' : '', 'y' : '', 'z' : '' },
        'pixel coordinates' : { 'x' : '', 'y' : '' },
    }
    """
    
    # World coordinates to Camera coordinates
    x_w = data['world coordinates']['x']
    y_w = data['world coordinates']['y']
    z_w = data['world coordinates']['z']
    
    world_coordinates_vector = np.array(
        [
            [x_w],
            [y_w],
            [z_w],
        ]
    )
    
    pitch_radians = math.radians(data['camera pose']['pitch'])
    yaw_radians = math.radians(data['camera pose']['yaw'])
    roll_radians = math.radians(data['camera pose']['roll'])
    
    pitch_rotate_matrix = np.array(
        [
            [math.cos(pitch_radians), 0, math.sin(pitch_radians)],
            [0, 1, 0],
            [-math.sin(pitch_radians), 0, math.cos(pitch_radians)],
        ]
    )
    
    yaw_rotate_matrix = np.array(
        [
            [math.cos(yaw_radians), -math.sin(yaw_radians), 0],
            [math.sin(yaw_radians), math.cos(yaw_radians), 0],
            [0, 0, 1],
        ]
    )
    
    roll_rotate_matrix = np.array(
        [
            [1, 0, 0],
            [0, math.cos(roll_radians), -math.sin(roll_radians)],
            [0, math.sin(roll_radians), math.cos(roll_radians)],
        ]
    )
    
    world_coordinates_vector_pitched = np.dot(pitch_rotate_matrix, world_coordinates_vector)
    world_coordinates_vector_pitched_yawed = np.dot(yaw_rotate_matrix, world_coordinates_vector_pitched)
    world_coordinates_vector_pitched_yawed_rolled = np.dot(roll_rotate_matrix, world_coordinates_vector_pitched_yawed)

    x_c = round(float(world_coordinates_vector_pitched_yawed_rolled[0][0]), 2)
    y_c = round(float(world_coordinates_vector_pitched_yawed_rolled[1][0]), 2)
    z_c = round(float(world_coordinates_vector_pitched_yawed_rolled[2][0]), 2)
    
    # Camera coordinates to Pixel coordinates
    distance = math.sqrt(x_c**2 + y_c**2 + z_c**2) # Distance to nodal point
    angle = math.degrees(math.acos(x_c / distance))
    fitting_func_coefs = [data['fitting func coefs']['x5'], data['fitting func coefs']['x4'], data['fitting func coefs']['x3'], data['fitting func coefs']['x2'], data['fitting func coefs']['x1'], data['fitting func coefs']['x0']]
    real_height = np.polyval(fitting_func_coefs, angle)
    azimuth_radians = math.atan2(z_c, -y_c)
    azimuth = (math.degrees(azimuth_radians) + 360 ) % 360
    
    pixel_size = data['sensor params']['pixel size']
    x_p = round((real_height / pixel_size) * math.cos(azimuth_radians), 2)
    y_p = round((real_height / pixel_size) * math.sin(azimuth_radians), 2)
    
    # Write data to memory
    data['camera coordinates'] = { 'x' : x_c, 'y' : y_c, 'z' : z_c }
    data['pixel coordinates'] = { 'x' : x_p, 'y' : y_p }
    
    return
        
def calculate_reverse(data):
    """ 
    data = {
        'world coordinates' : { 'x' : '', 'y' : '', 'z' : '' },
        'fitting func coefs' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'fitting func coefs reverse' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'camera pose' : { 'pitch' : '', 'yaw' : '', 'roll' : '' },
        'sensor params' : { 'width' : '', 'height' : '', 'pixel size' : '' },
        'camera coordinates' : { 'x' : '', 'y' : '', 'z' : '' },
        'pixel coordinates' : { 'x' : '', 'y' : '' },
    }
    """
    # Pixel coordinates to Camera coordinatess
    x_p = data['pixel coordinates']['x']
    y_p = data['pixel coordinates']['y']
    fitting_func_coefs_reverse = [
        data['fitting func coefs reverse']['x5'], 
        data['fitting func coefs reverse']['x4'], 
        data['fitting func coefs reverse']['x3'], 
        data['fitting func coefs reverse']['x2'], 
        data['fitting func coefs reverse']['x1'], 
        data['fitting func coefs reverse']['x0'],
    ]
    x_c = 2000
    
    real_height = math.sqrt(x_p**2 + y_p**2)
    azimuth_on_sensor = (math.degrees(math.atan2(x_p, -y_p)) + 270) % 360 
    angle = np.polyval(fitting_func_coefs_reverse, real_height)
    distance = math.tan(math.radians(angle)) * x_c # Distance from nodal point of world coordinates
    y_c = round(distance * math.cos(math.radians(azimuth_on_sensor)), 2)
    z_c = round(distance * math.sin(math.radians(azimuth_on_sensor)), 2)
    
    x_p = x_c
    y_p = y_c
    z_p = z_c
    
    # Write data to memory
    data['camera coordinates'] = { 'x' : x_c, 'y' : y_c, 'z' : z_c }
    data['world coordinates'] = {'x' : x_p, 'y' : y_p, 'z' : z_p }

    return