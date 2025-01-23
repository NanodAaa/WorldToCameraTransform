# gui.py

import re
import os
import tkinter as tk

class W2CTransform():
    configuration_filename = 'configuration.txt'
    configuration_filepath = os.path.join(os.path.dirname(__file__), configuration_filename)
    
    label_format_dict = { 'font' : ('consolas', 14), 'padx' : 5, 'pady' : 5, 'sticky' : 'w', 'width' : 13 }
    entry_format_dict = { 'font' : ('consolas', 14), 'padx' : 5, 'pady' : 5, 'sticky' : 'ew', 'width' : 13 }
    button_format_dict = { 'bg' : 'lightblue', 'padx' : 5, 'pady' : 5, 'sticky' : 'ewsn', 'width' : 13 }
    
    pattern_dict = { 
                    'world coordinates' : 'World Coordinates:\s*\[([-+]?\d+\.\d+|\d+),\s*([-+]?\d+\.\d+|\d+),\s*([-+]?\d+\.\d+|\d+)\]',
                    'fitting func coefs' : 'Fitting Function Coefficients:\s*\[([-+]?\d+(\.\d+)?[eE][-+]?\d+),\s*([-+]?\d+(\.\d+)?[eE][-+]?\d+),\s*([-+]?\d+(\.\d+)?[eE][-+]?\d+),\s*([-+]?\d+(\.\d+)?[eE][-+]?\d+),\s*([-+]?\d+(\.\d+)?[eE][-+]?\d+),\s*([-+]?\d+(\.\d+)?[eE][-+]?\d+)\]',
                    'camera pose' : 'Camera Pose:\s*\[([-+]?\d+\.\d+|\d+),\s*([-+]?\d+\.\d+|\d+),\s*([-+]?\d+\.\d+|\d+)\]',
                    'sensor params' : 'Sensor Params:\s*\[(\d+),\s*(\d+),\s*([-+]?\d+\.\d+E[-+]?\d+)\]',
                    }
    
    world_coordinates = [] # World coordinates compare to Ref coordinate.
    fitting_func_coefs = [] # Fitting function coefficients X^6 (x6 -> x1).
    camera_pose = []    # Camera pose compare to world coordinates.
    
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.read_configuration_from_file()
    
    def read_configuration_from_file(self):
        """ 
        Read configuration from file.
        """
        if os.path.exists(self.configuration_filepath):
            with open(self.configuration_filepath, mode='r') as f:
                data = f.read()
                
                # World Coordinates
                matches = re.search(self.pattern_dict['world coordinates'], data)
                self.world_coordinates = [float(matches.group(1)), float(matches.group(2)), float(matches.group(3))]
                print(self.world_coordinates)
                
                # Fitting Function Coefficients
                matches = re.search(self.pattern_dict['fitting func coefs'], data)
                for i in range(0, 6):
                    self.fitting_func_coefs[i] = matches.group(i+1)
                    
                print(self.fitting_func_coefs)
                
                # Camera Pose
                matches = re.search(self.pattern_dict['camera pose'], data)
                self.camera_pose = [float(matches.group(1)), float(matches.group(2)), float(matches.group(3))]
                print(self.camera_pose)
                
                # Sensor Params
                matches = re.search(self.pattern_dict['sensor params'], data)
                self.sensor_params = [int(matches.group(1)), int(matches.group(2)), float(matches.group(3))]
                print(self.sensor_params)
                
                f.close()

    def set_init_window(self):
        self.init_window_name = tk.Tk()
        self.init_window_name.title('W2CTransform')
        
        # World Coordinates
        self.world_coordinate_label = tk.Label(self.init_window_name, text='P_w: ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.world_coordinate_label.grid(row=0, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])

        self.world_coordinate_x_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_x_entry.grid(row=0, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_x_entry.insert(0, self.world_coordinates[0])
        
        self.world_coordinate_y_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_y_entry.grid(row=0, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_y_entry.insert(0, self.world_coordinates[1])
        
        self.world_coordinate_z_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.world_coordinate_z_entry.grid(row=0, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.world_coordinate_z_entry.insert(0, self.world_coordinates[2])
        
        # Camera Pose
        self.camera_pose_label = tk.Label(self.init_window_name, text='Pose: ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.camera_pose_label.grid(row=1, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.camera_pose_yaw_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_yaw_entry.grid(row=1, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_yaw_entry.insert(0, self.camera_pose[0])
        
        self.camera_pose_pitch_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_pitch_entry.grid(row=1, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_pitch_entry.insert(0, self.camera_pose[1])
        
        self.camera_pose_roll_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.camera_pose_roll_entry.grid(row=1, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.camera_pose_roll_entry.insert(0, self.camera_pose[2])
        
        # Fitting Function Coefficients
        self.fitting_func_coefs_label = tk.Label(self.init_window_name, text='FitCoefs: ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.fitting_func_coefs_label.grid(row=2, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.fitting_func_coefs_x5_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x5_entry.grid(row=2, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x5_entry.insert(0, self.fitting_func_coefs[0])
        
        self.fitting_func_coefs_x4_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x4_entry.grid(row=2, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x4_entry.insert(0, self.fitting_func_coefs[1])
        
        self.fitting_func_coefs_x3_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x3_entry.grid(row=2, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x3_entry.insert(0, self.fitting_func_coefs[2])
        
        self.fitting_func_coefs_x2_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x2_entry.grid(row=2, column=4, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x2_entry.insert(0, self.fitting_func_coefs[3])
        
        self.fitting_func_coefs_x1_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x1_entry.grid(row=2, column=5, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x1_entry.insert(0, self.fitting_func_coefs[4])
        
        self.fitting_func_coefs_x0_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.fitting_func_coefs_x0_entry.grid(row=2, column=6, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.fitting_func_coefs_x0_entry.insert(0, self.fitting_func_coefs[5])
        
        # Sensor Params
        self.sensor_params_label = tk.Label(self.init_window_name, text='SensrParams: ', font=self.label_format_dict['font'], width=self.label_format_dict['width'])
        self.sensor_params_label.grid(row=3, column=0, padx=self.label_format_dict['padx'], pady=self.label_format_dict['pady'], sticky=self.label_format_dict['sticky'])
        
        self.sensor_params_width_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_width_entry.grid(row=3, column=1, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_width_entry.insert(0, self.sensor_params[0])
        
        self.sensor_params_height_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_height_entry.grid(row=3, column=2, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_height_entry.insert(0, self.sensor_params[1])
        
        self.sensor_params_pixel_size_entry = tk.Entry(self.init_window_name, font=self.entry_format_dict['font'], width=self.entry_format_dict['width'])
        self.sensor_params_pixel_size_entry.grid(row=3, column=3, padx=self.entry_format_dict['padx'], pady=self.entry_format_dict['pady'], sticky=self.entry_format_dict['sticky'])
        self.sensor_params_pixel_size_entry.insert(0, self.sensor_params[2])
        
        # Calculate Button
        self.calculate_button = tk.Button(self.init_window_name, text='Calculate', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'],command=self.calculate)
        self.calculate_button.grid(row=4, column=0, padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])
                
        # Save Button
        self.calculate_button = tk.Button(self.init_window_name, text='Save', bg=self.button_format_dict['bg'], width=self.button_format_dict['width'],command=self.save)
        self.calculate_button.grid(row=4, column=1, padx=self.button_format_dict['padx'], pady=self.button_format_dict['pady'], sticky=self.button_format_dict['sticky'])        
                
    def calculate(self):
        self.read_configuration_from_file()
        
        return
        
    def save(self):
        self.world_coordinates = [float(self.world_coordinate_x_entry.get()), float(self.world_coordinate_y_entry.get()), float(self.world_coordinate_z_entry.get())]
        self.fitting_func_coefs = [float(self.fitting_func_coefs_x5_entry.get()), float(self.fitting_func_coefs_x4_entry.get()), float(self.fitting_func_coefs_x3_entry.get()), float(self.fitting_func_coefs_x2_entry.get()), float(self.fitting_func_coefs_x1_entry.get()), float(self.fitting_func_coefs_x0_entry.get())]
        self.camera_pose = [float(self.camera_pose_yaw_entry.get()), float(self.camera_pose_pitch_entry.get()), float(self.camera_pose_roll_entry.get())]
        self.sensor_params = [int(self.sensor_params_width_entry.get()), int(self.sensor_params_height_entry.get()), float(self.sensor_params_pixel_size_entry.get())]
        
        if os.path.exists(self.configuration_filepath):
            with open(self.configuration_filepath, 'w') as f:
                f.writelines(['World Coordinates: ', str(self.world_coordinates), '\n'])
                f.writelines(['Fitting Function Coefficients: ', str(self.fitting_func_coefs), '\n'])
                f.writelines(['Camera Pose: ', str(self.camera_pose), '\n'])
                f.writelines(['Sensor Params: ', str(self.sensor_params), '\n'])

                f.close()
                
        return
        
    def start(self):
        self.set_init_window()
        self.init_window_name.mainloop()
        