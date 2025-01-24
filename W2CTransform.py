# W2CTransform.py

import math
import json
import os
import numpy as np
import tkinter as tk

class W2CTransform():
    data_filename = 'data.json'
    data_filepath = os.path.join(os.path.dirname(__file__), data_filename)
    
    entry_list = []
    
    label_format_dict = { 'font' : ('consolas', 14), 'padx' : 5, 'pady' : 5, 'sticky' : 'w', 'width' : 13 }
    entry_format_dict = { 'font' : ('consolas', 14), 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 13 }
    button_format_dict = { 'bg' : 'lightblue', 'padx' : 5, 'pady' : 5, 'sticky' : 'ewsn', 'width' : 13 }
    
    data = {
        'world coordinates' : { 'x' : 0.0, 'y' : 0.0, 'z' : 0.0 },
        'fitting func coefs' : { 'x5' : 0.0, 'x4' : 0.0, 'x3' : 0.0, 'x2' : 0.0, 'x1' : 0.0, 'x0' : 0.0 },
        'camera pose' : { 'pitch' : 0.0, 'yaw' : 0.0, 'roll' : 0.0, 'pitch radians' : 0.0, 'yaw radians' : 0.0, 'roll radians' : 0.0 },
        'sensor params' : { 'width' : 0, 'height' : 0, 'pixel size' : 0.0 },
    }
    
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.load_data_from_json()
    
    def load_data_from_json(self):
        """ 
        Read configuration from file.
        """
        if os.path.exists(self.data_filepath):
            with open(self.data_filepath, 'r') as f:
                self.data = json.load(f)                
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
        self.world_coordinate_label = tk.Label(self.init_window_name, text='P_w: ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
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
        self.camera_pose_label = tk.Label(self.init_window_name, text='Pose: ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
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
        self.fitting_func_coefs_label = tk.Label(self.init_window_name, text='FitCoefs: ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
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
        self.sensor_params_label = tk.Label(self.init_window_name, text='SensrParams: ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
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
        
        # Calculate Button
        self.calculate_button = tk.Button(self.init_window_name, text='Calculate', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'],command=self.onclick_button_calculate)
        self.calculate_button.grid(row=4, column=0, padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])
                
        # Save Button
        self.calculate_button = tk.Button(self.init_window_name, text='Save', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'],command=self.onclick_button_save)
        self.calculate_button.grid(row=4, column=1, padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])        
                
    def onclick_button_save(self):
        self.save_data_to_memory()
        self.save_data_to_json()
        self.refresh_data_in_gui()
        return
                
    def onclick_button_calculate(self):
        self.calculate()
        return
                
    def calculate(self):
        self.save_data_to_memory()
        
        # Pitch Transform
        pitch_radians =  self.data['camera pose']['pitch radians'] = math.radians(self.data['camera pose']['pitch'])
        yaw_radians = self.data['camera pose']['yaw radians'] = math.radians(self.data['camera pose']['yaw'])
        roll_radians = self.data['camera pose']['roll radians'] = math.radians(self.data['camera pose']['roll'])
        
        x = self.data['world coordinates']['x']
        y = self.data['world coordinates']['y']
        z = self.data['world coordinates']['z']
        
        world_coordinates_vector = np.array(
            [
                [x],
                [y],
                [z],
            ]
        )
        pitch_rotate_matrix = np.array(
            [
                [math.cos(pitch_radians), 0, math.sin(pitch_radians)],
                [0, 1, 0],
                [-math.sin(pitch_radians), 0, math.cos(pitch_radians)],
            ]      
        )
        
        yaw_rorate_matrix = np.array(
            [
                [math.cos(yaw_radians), -math.sin(yaw_radians), 0],
                [math.sin(yaw_radians), math.cos(yaw_radians), 0],
                [0, 0, 1],
            ]
        )
        
        world_coordinates_vector_pitched = np.dot(pitch_rotate_matrix, world_coordinates_vector)
#        print(world_coordinates_vector_pitched)
        
        world_coordinates_vector_pitched_yawed = np.dot(yaw_rorate_matrix, world_coordinates_vector_pitched)
#        print(world_coordinates_vector_pitched_yawed)
        
        return
        
    def save_data_to_memory(self):         
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
        
        self.world_coordinate_x_entry.insert(0, self.data['world coordinates']['x'])
        self.world_coordinate_y_entry.insert(0, self.data['world coordinates']['y'])
        self.world_coordinate_z_entry.insert(0, self.data['world coordinates']['z'])
        self.camera_pose_pitch_entry.insert(0, self.data['camera pose']['pitch'])
        self.camera_pose_yaw_entry.insert(0, self.data['camera pose']['yaw'])
        self.camera_pose_roll_entry.insert(0, self.data['camera pose']['roll'])
        self.fitting_func_coefs_x5_entry.insert(0, self.data['fitting func coefs']['x5'])
        self.fitting_func_coefs_x4_entry.insert(0, self.data['fitting func coefs']['x4'])
        self.fitting_func_coefs_x3_entry.insert(0, self.data['fitting func coefs']['x3'])
        self.fitting_func_coefs_x2_entry.insert(0, self.data['fitting func coefs']['x2'])
        self.fitting_func_coefs_x1_entry.insert(0, self.data['fitting func coefs']['x1'])
        self.fitting_func_coefs_x0_entry.insert(0, self.data['fitting func coefs']['x0'])
        self.sensor_params_width_entry.insert(0, self.data['sensor params']['width'])
        self.sensor_params_height_entry.insert(0, self.data['sensor params']['height'])
        self.sensor_params_pixel_size_entry.insert(0, self.data['sensor params']['pixel size'])
        
    def start(self):
        self.set_init_window()
        self.init_window_name.mainloop()
        
if __name__ == '__main__':
    mygui = W2CTransform('root')
    mygui.start()
    
    exit()