# W2CTransform.py

import math
import json
import os
import sys
import numpy as np
import tkinter as tk

class W2CTransform():
    data_filename = 'data.json'
    data_filepath = os.path.join(os.path.dirname(__file__), data_filename)
    
    entry_list = []
    
    label_format_dict = { 'font' : ('consolas', 11), 'padx' : 5, 'pady' : 5, 'sticky' : 'w', 'width' : 14 }
    entry_format_dict = { 'font' : ('consolas', 12), 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 13 }
    button_format_dict = { 'bg' : 'lightblue', 'padx' : 5, 'pady' : 5, 'sticky' : 'ewsn', 'width' : 13 }
    
    data = {
        'world coordinates' : { 'x' : '', 'y' : '', 'z' : '' },
        'fitting func coefs' : { 'x5' : '', 'x4' : '', 'x3' : '', 'x2' : '', 'x1' : '', 'x0' : '' },
        'camera pose' : { 'pitch' : '', 'yaw' : '', 'roll' : '' },
        'sensor params' : { 'width' : '', 'height' : '', 'pixel size' : '' },
        'camera coordinates' : { 'x' : '', 'y' : '', 'z' : '' },
        'pixel coordinates' : { 'x' : '', 'y' : '' },
    }
    
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.get_data_json_path()
        self.load_data_from_json()
    
    def get_data_json_path(self):
        for dirpath, dirnames, filenames in os.walk(os.path.dirname(__file__)):
            if self.data_filename in filenames:
                self.data_filepath = os.path.join(dirpath, self.data_filename)
                return
    
    def load_data_from_json(self):
        """ 
        Read configuration from file.
        """
        if os.path.exists(self.data_filepath):
            with open(self.data_filepath, 'r') as f:
                self.data = json.load(f) # Data in memory               
                f.close()
                
        else:
            with open(self.data_filepath, 'w') as f:
                json.dump(self.data, f)                
                f.close()

    def set_init_window(self):
        # root
        self.init_window_name = tk.Tk()
        self.init_window_name.title('W2CTransform')
        
        # World Coordinates
        self.world_coordinate_label = tk.Label(self.init_window_name, text='P_w(XYZ): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.world_coordinate_label.grid(row=0, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])

        self.world_coordinate_x_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_x_entry.grid(row=0, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_x_entry.insert(0, self.data['world coordinates']['x'])
        self.entry_list.append(self.world_coordinate_x_entry)
        
        self.world_coordinate_y_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_y_entry.grid(row=0, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_y_entry.insert(0, self.data['world coordinates']['y'])
        self.entry_list.append(self.world_coordinate_y_entry)
        
        self.world_coordinate_z_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_z_entry.grid(row=0, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_z_entry.insert(0, self.data['world coordinates']['z'])
        self.entry_list.append(self.world_coordinate_z_entry)
        
        # Camera Pose
        self.camera_pose_label = tk.Label(self.init_window_name, text='Pose(PYR): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.camera_pose_label.grid(row=1, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.camera_pose_pitch_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_pitch_entry.grid(row=1, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_pitch_entry.insert(0, self.data['camera pose']['pitch'])
        self.entry_list.append(self.camera_pose_pitch_entry)
        
        self.camera_pose_yaw_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_yaw_entry.grid(row=1, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_yaw_entry.insert(0, self.data['camera pose']['yaw'])
        self.entry_list.append(self.camera_pose_yaw_entry)
        
        
        self.camera_pose_roll_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_roll_entry.grid(row=1, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_roll_entry.insert(0, self.data['camera pose']['roll'])
        self.entry_list.append(self.camera_pose_roll_entry)
        
        # Fitting Function Coefficients
        self.fitting_func_coefs_label = tk.Label(self.init_window_name, text='FitCoe(X5>0): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.fitting_func_coefs_label.grid(row=2, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.fitting_func_coefs_x5_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x5_entry.grid(row=2, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x5_entry.insert(0, self.data['fitting func coefs']['x5'])
        self.entry_list.append(self.fitting_func_coefs_x5_entry)
        
        self.fitting_func_coefs_x4_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x4_entry.grid(row=2, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x4_entry.insert(0, self.data['fitting func coefs']['x4'])
        self.entry_list.append(self.fitting_func_coefs_x4_entry)
        
        self.fitting_func_coefs_x3_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x3_entry.grid(row=2, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x3_entry.insert(0, self.data['fitting func coefs']['x3'])
        self.entry_list.append(self.fitting_func_coefs_x3_entry)
        
        self.fitting_func_coefs_x2_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x2_entry.grid(row=2, column=4, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x2_entry.insert(0, self.data['fitting func coefs']['x2'])
        self.entry_list.append(self.fitting_func_coefs_x2_entry)
        
        self.fitting_func_coefs_x1_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x1_entry.grid(row=2, column=5, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x1_entry.insert(0, self.data['fitting func coefs']['x1'])
        self.entry_list.append(self.fitting_func_coefs_x1_entry)
        
        self.fitting_func_coefs_x0_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x0_entry.grid(row=2, column=6, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x0_entry.insert(0, self.data['fitting func coefs']['x0'])
        self.entry_list.append(self.fitting_func_coefs_x0_entry)
        
        # Sensor Params
        self.sensor_params_label = tk.Label(self.init_window_name, text='SenPrms(WHP): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_params_label.grid(row=3, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_params_width_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_width_entry.grid(row=3, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_width_entry.insert(0, self.data['sensor params']['width'])
        self.entry_list.append(self.sensor_params_width_entry)
        
        self.sensor_params_height_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_height_entry.grid(row=3, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_height_entry.insert(0, self.data['sensor params']['height'])
        self.entry_list.append(self.sensor_params_height_entry)
        
        self.sensor_params_pixel_size_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_pixel_size_entry.grid(row=3, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_pixel_size_entry.insert(0, self.data['sensor params']['pixel size'])
        self.entry_list.append(self.sensor_params_pixel_size_entry)
        
        # camera Coordinates
        self.camera_corrdinates_label = tk.Label(self.init_window_name, text='P_c(XYZ): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.camera_corrdinates_label.grid(row=4, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.camera_corrdinates_x_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_corrdinates_x_entry.grid(row=4, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_corrdinates_x_entry.insert(0, self.data['camera coordinates']['x'])
        self.camera_corrdinates_x_entry.config(state='readonly') # Set entry to read only
        self.entry_list.append(self.camera_corrdinates_x_entry)
        
        self.camera_corrdinates_y_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_corrdinates_y_entry.grid(row=4, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_corrdinates_y_entry.insert(0, self.data['camera coordinates']['y'])
        self.camera_corrdinates_y_entry.config(state='readonly') # Set entry to read only
        self.entry_list.append(self.camera_corrdinates_y_entry)
        
        self.camera_corrdinates_z_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_corrdinates_z_entry.grid(row=4, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_corrdinates_z_entry.insert(0, self.data['camera coordinates']['z'])
        self.camera_corrdinates_z_entry.config(state='readonly') # Set entry to read only
        self.entry_list.append(self.camera_corrdinates_z_entry)
        
        # Pixel Coordinates
        self.pixel_coordinates_label = tk.Label(self.init_window_name, text='P_p(XY): ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.pixel_coordinates_label.grid(row=5, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.pixel_coordinate_x_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.pixel_coordinate_x_entry.grid(row=5, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.pixel_coordinate_x_entry.insert(0, self.data['pixel coordinates']['x'])
        self.pixel_coordinate_x_entry.config(state='readonly') # Set entry to read only
        self.entry_list.append(self.pixel_coordinate_x_entry)
        
        self.pixel_coordinate_y_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.pixel_coordinate_y_entry.grid(row=5, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.pixel_coordinate_y_entry.insert(0, self.data['pixel coordinates']['y'])
        self.pixel_coordinate_y_entry.config(state='readonly') # Set entry to read only
        self.entry_list.append(self.pixel_coordinate_y_entry)
        
        # Calculate Button
        self.calculate_button = tk.Button(self.init_window_name, text='Calculate', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'], command=self.onclick_button_calculate)
        self.calculate_button.grid(row=6, column=0, padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])
                
        # Save Button
        self.save_button = tk.Button(self.init_window_name, text='Save', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'], command=self.onclick_button_save)
        self.save_button.grid(row=6, column=1, padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])        

        # Positive Button
        self.positive_button = tk.Button(self.init_window_name, text='Positive', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'], command=self.positive)
        self.positive_button.grid(row=6, column=2, padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])
        
        # Reverse Button
        self.reverse_button = tk.Button(self.init_window_name, text='Reverse', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'], command=self.reverse)
        self.reverse_button.grid(row=6, column=3, padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])
                
    def onclick_button_positive(self):
        self.positive()
    
    def positive(self):
        return
              
    def onclick_button_reverse(self):
        self.reverse()
    
    def reverse(self):
        return
                
    def onclick_button_save(self):
        if self.save_data_from_entry_to_memory() == -1:
            return
        
        if self.save_data_to_json() == -1:
            return

        if self.refresh_data_in_gui() == -1:
            return
        
        return
                
    def onclick_exit(self):
        self.exit()
        
    def exit(self):
        sys.exit()
                
    def onclick_button_calculate(self):
        self.calculate()
        self.refresh_data_in_gui()
        self.save_data_from_entry_to_memory()
        self.save_data_to_json()
        return
                
    def calculate(self):
        self.save_data_from_entry_to_memory()
        
        x_w = self.data['world coordinates']['x']
        y_w = self.data['world coordinates']['y']
        z_w = self.data['world coordinates']['z']
        
        world_coordinates_vector = np.array(
            [
                [x_w],
                [y_w],
                [z_w],
            ]
        )
        
        # Pitch Transform
        pitch_radians = math.radians(self.data['camera pose']['pitch'])
        yaw_radians = math.radians(self.data['camera pose']['yaw'])
        roll_radians = math.radians(self.data['camera pose']['roll'])
        
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

        x_c = float(world_coordinates_vector_pitched_yawed_rolled[0][0])
        y_c = float(world_coordinates_vector_pitched_yawed_rolled[1][0])
        z_c = float(world_coordinates_vector_pitched_yawed_rolled[2][0])
        
        distance = math.sqrt(x_c**2 + y_c**2 + z_c**2)
        angle = math.degrees(math.acos(x_c / distance))
        fitting_func_coefs = [self.data['fitting func coefs']['x5'], self.data['fitting func coefs']['x4'], self.data['fitting func coefs']['x3'], self.data['fitting func coefs']['x2'], self.data['fitting func coefs']['x1'], self.data['fitting func coefs']['x0']]
        pixel_to_image_distance = real_height = np.polyval(fitting_func_coefs, angle)
        azimuth_radians = math.atan2(z_c, -y_c)
        azimuth = (math.degrees(azimuth_radians) + 360 ) % 360
        
        pixel_size = self.data['sensor params']['pixel size']
        x_p = (pixel_to_image_distance / pixel_size) * math.cos(azimuth_radians)
        y_p = (pixel_to_image_distance / pixel_size) * math.sin(azimuth_radians)
        
        self.data['camera coordinates'] = { 'x' : x_c, 'y' : y_c, 'z' : z_c }
        self.data['pixel coordinates'] = { 'x' : x_p, 'y' : y_p }
        
#        print(world_coordinates_vector_pitched)
#        print(world_coordinates_vector_pitched_yawed)
#        print(world_coordinates_vector_pitched_yawed_rolled)
#        print(real_height)
#        print(azimuth)
#        print(x_p, y_p)
        
        return
        
    def save_data_from_entry_to_memory(self):      
        """
        Save data to memory. 
        """   
        """ for entry in self.entry_list:
            if entry.get() == '':
                return -1 """
        
        self.data['world coordinates'] = { 
            'x' : float(self.world_coordinate_x_entry.get().replace('E', 'e')), 'y' : float(self.world_coordinate_y_entry.get().replace('E', 'e')), 'z' : float(self.world_coordinate_z_entry.get().replace('E', 'e')) }
        self.data['fitting func coefs'] = { 
            'x5' : float(self.fitting_func_coefs_x5_entry.get().replace('E', 'e')), 'x4' : float(self.fitting_func_coefs_x4_entry.get().replace('E', 'e')),
            'x3' : float(self.fitting_func_coefs_x3_entry.get().replace('E', 'e')), 'x2' : float(self.fitting_func_coefs_x2_entry.get().replace('E', 'e')),
            'x1' : float(self.fitting_func_coefs_x1_entry.get().replace('E', 'e')), 'x0' : float(self.fitting_func_coefs_x0_entry.get().replace('E', 'e')),
        }
        self.data['camera pose'] = { 
            'pitch' : float(self.camera_pose_pitch_entry.get().replace('E', 'e')), 'yaw' : float(self.camera_pose_yaw_entry.get().replace('E', 'e')), 'roll' : float(self.camera_pose_roll_entry.get().replace('E', 'e')) }
        self.data['sensor params'] = { 
            'width' : int(self.sensor_params_width_entry.get()), 'height' : int(self.sensor_params_height_entry.get()), 'pixel size' : float(self.sensor_params_pixel_size_entry.get().replace('E', 'e')) }       
           
        return
    
    def save_data_to_json(self):
        if os.path.exists(self.data_filepath):
            with open(self.data_filepath, 'w') as f:          
                json.dump(self.data, f)

                f.close()
    
    def clear_data_in_gui(self):
        for entry in self.entry_list:
            entry.delete(0, tk.END)
    
    def refresh_data_in_gui(self):
        self.clear_data_in_gui()
        
        # World coordinates
        self.world_coordinate_x_entry.insert(0, self.data['world coordinates']['x'])
        self.world_coordinate_y_entry.insert(0, self.data['world coordinates']['y'])
        self.world_coordinate_z_entry.insert(0, self.data['world coordinates']['z'])
        # Pose
        self.camera_pose_pitch_entry.insert(0, self.data['camera pose']['pitch'])
        self.camera_pose_yaw_entry.insert(0, self.data['camera pose']['yaw'])
        self.camera_pose_roll_entry.insert(0, self.data['camera pose']['roll'])
        # Fitting funcion coefficients
        self.fitting_func_coefs_x5_entry.insert(0, self.data['fitting func coefs']['x5'])
        self.fitting_func_coefs_x4_entry.insert(0, self.data['fitting func coefs']['x4'])
        self.fitting_func_coefs_x3_entry.insert(0, self.data['fitting func coefs']['x3'])
        self.fitting_func_coefs_x2_entry.insert(0, self.data['fitting func coefs']['x2'])
        self.fitting_func_coefs_x1_entry.insert(0, self.data['fitting func coefs']['x1'])
        self.fitting_func_coefs_x0_entry.insert(0, self.data['fitting func coefs']['x0'])
        # Sensor params
        self.sensor_params_width_entry.insert(0, self.data['sensor params']['width'])
        self.sensor_params_height_entry.insert(0, self.data['sensor params']['height'])
        self.sensor_params_pixel_size_entry.insert(0, self.data['sensor params']['pixel size'])
        # Camera coordinates
        self.camera_corrdinates_x_entry.insert(0, self.data['camera coordinates']['x'])
        self.camera_corrdinates_y_entry.insert(0, self.data['camera coordinates']['y'])
        self.camera_corrdinates_z_entry.insert(0, self.data['camera coordinates']['z'])
        # Pixel coordinates
        self.pixel_coordinate_x_entry.insert(0, self.data['pixel coordinates']['x'])
        self.pixel_coordinate_y_entry.insert(0, self.data['pixel coordinates']['y'])
        
    def start(self):
        self.set_init_window()
        self.init_window_name.protocol("WM_DELETE_WINDOW", self.onclick_exit) # Bind exit button to onclick_exit()
        self.init_window_name.mainloop()
        
if __name__ == '__main__':
    mygui = W2CTransform('root')
    mygui.start()
    
    exit()