# gui.py
import tkinter as tk

class myGUI():
    LABEL_FORMAT_DICT = { 'font' : ('consolas', 16), 'padx' : 10, 'pady' : 10, 'sticky' : 'w' }
    ENTRY_FORMAT_DICT = { 'font' : ('consolas', 14), 'padx' : 10, 'pady' : 10, 'sticky' : 'w' }
    ENTRY_FORMAT_DICT_S = { 'font' : ('consolas', 14), 'padx' : 5, 'pady' : 5, 'sticky' : 'w' }
    
    fitting_func_coefs = [] # Fitting function coefficients X^6 (x6 -> x1)
    
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
    
    def set_init_window(self):
        self.init_window_name = tk.Tk()
        self.init_window_name.title('W2CTransform')
        
        # World Coordinates
        self.world_coordinate_label = tk.Label(self.init_window_name, text='World Coordinate: ', font=self.LABEL_FORMAT_DICT['font'])
        self.world_coordinate_label.grid(row=0, column=0, padx=self.LABEL_FORMAT_DICT['padx'], pady=self.LABEL_FORMAT_DICT['pady'], sticky=self.LABEL_FORMAT_DICT['sticky'])

        self.world_coordinate_x_entry = tk.Entry(self.init_window_name, font=self.ENTRY_FORMAT_DICT['font'])
        self.world_coordinate_x_entry.grid(row=0, column=1, padx=self.ENTRY_FORMAT_DICT_S['padx'], pady=self.ENTRY_FORMAT_DICT_S['pady'], sticky=self.ENTRY_FORMAT_DICT_S['sticky'])
        
        self.world_coordinate_y_entry = tk.Entry(self.init_window_name, font=self.ENTRY_FORMAT_DICT['font'])
        self.world_coordinate_y_entry.grid(row=0, column=2, padx=self.ENTRY_FORMAT_DICT_S['padx'], pady=self.ENTRY_FORMAT_DICT_S['pady'], sticky=self.ENTRY_FORMAT_DICT_S['sticky'])
        
        self.world_coordinate_z_entry = tk.Entry(self.init_window_name, font=self.ENTRY_FORMAT_DICT['font'])
        self.world_coordinate_z_entry.grid(row=0, column=3, padx=self.ENTRY_FORMAT_DICT_S['padx'], pady=self.ENTRY_FORMAT_DICT_S['pady'], sticky=self.ENTRY_FORMAT_DICT_S['sticky'])
        
        
    def start(self):
        self.set_init_window()
        self.init_window_name.mainloop()
        