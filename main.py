import tkinter as tk
from tkinter import filedialog, messagebox
import os
from watermarker import add_text_watermark, add_logo_watermark

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarker")
        self.root.geometry("500x400")
        
        # State variables
        self.image_path = tk.StringVar()
        self.watermark_type = tk.StringVar(value="text")
        self.watermark_text = tk.StringVar()
        self.logo_path = tk.StringVar()
        self.compress_output = tk.BooleanVar(value=False)
        
        self.create_widgets()
        
    def create_widgets(self):
        # 1. Image Selection
        frame_img = tk.LabelFrame(self.root, text="Step 1: Select Image", padx=10, pady=10)
        frame_img.pack(fill="x", padx=10, pady=5)
        
        tk.Entry(frame_img, textvariable=self.image_path, state="readonly", width=40).pack(side="left", padx=(0, 10))
        tk.Button(frame_img, text="Browse", command=self.browse_image).pack(side="left")
        
        # 2. Watermark Type
        frame_type = tk.LabelFrame(self.root, text="Step 2: Watermark Type", padx=10, pady=10)
        frame_type.pack(fill="x", padx=10, pady=5)
        
        tk.Radiobutton(frame_type, text="Text", variable=self.watermark_type, value="text", command=self.toggle_inputs).pack(anchor="w")
        
        self.text_frame = tk.Frame(frame_type)
        self.text_frame.pack(fill="x", padx=20)
        tk.Label(self.text_frame, text="Watermark Text:").pack(side="left")
        tk.Entry(self.text_frame, textvariable=self.watermark_text, width=30).pack(side="left", padx=(10, 0))
        
        tk.Radiobutton(frame_type, text="Logo Image", variable=self.watermark_type, value="logo", command=self.toggle_inputs).pack(anchor="w", pady=(10, 0))
        
        self.logo_frame = tk.Frame(frame_type)
        self.logo_frame.pack(fill="x", padx=20)
        tk.Entry(self.logo_frame, textvariable=self.logo_path, state="readonly", width=30).pack(side="left")
        tk.Button(self.logo_frame, text="Browse Logo", command=self.browse_logo).pack(side="left", padx=(10, 0))
        
        # 3. Output Options
        frame_opt = tk.LabelFrame(self.root, text="Step 3: Output Options", padx=10, pady=10)
        frame_opt.pack(fill="x", padx=10, pady=5)
        
        tk.Checkbutton(frame_opt, text="Compress Output Image (lower quality)", variable=self.compress_output).pack(anchor="w")
        
        # 4. Action Buttons
        frame_action = tk.Frame(self.root, pady=10)
        frame_action.pack(fill="x", padx=10)
        
        tk.Button(frame_action, text="Apply Watermark & Save", command=self.process_watermark, height=2, bg="green").pack(fill="x")
        
        self.toggle_inputs()
        
    def toggle_inputs(self):
        if self.watermark_type.get() == "text":
            for child in self.text_frame.winfo_children():
                child.configure(state="normal")
            for child in self.logo_frame.winfo_children():
                child.configure(state="disabled")
        else:
            for child in self.text_frame.winfo_children():
                child.configure(state="disabled")
            for child in self.logo_frame.winfo_children():
                child.configure(state="normal")
                
    def browse_image(self):
        filepath = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        if filepath:
            self.image_path.set(filepath)
            
    def browse_logo(self):
        filepath = filedialog.askopenfilename(
            title="Select a Logo",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )
        if filepath:
            self.logo_path.set(filepath)
            
    def process_watermark(self):
        img_path = self.image_path.get()
        if not img_path:
            messagebox.showerror("Error", "Please select an image first.")
            return
            
        # Determine output path
        dir_name, file_name = os.path.split(img_path)
        name, ext = os.path.splitext(file_name)
        
        # Check compression
        is_compressed = self.compress_output.get()
        
        # File increment logic
        idx = 1
        while True:
            # e.g. watermarked_01_myphoto.jpg
            out_name = f"watermarked_{idx:02d}_{name}{ext}"
            out_path = os.path.join(dir_name, out_name)
            if not os.path.exists(out_path):
                break
            idx += 1
        
        w_type = self.watermark_type.get()
        success = False
        
        if w_type == "text":
            text = self.watermark_text.get()
            if not text:
                messagebox.showerror("Error", "Please enter watermark text.")
                return
            success = add_text_watermark(img_path, text, out_path, is_compressed)
        else:
            logo_path = self.logo_path.get()
            if not logo_path:
                messagebox.showerror("Error", "Please select a logo image.")
                return
            success = add_logo_watermark(img_path, logo_path, out_path, is_compressed)
            
        if success:
            messagebox.showinfo("Success", f"Watermarked image saved to:\n{out_path}")
        else:
            messagebox.showerror("Error", "Failed to apply watermark. Check console for details.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
