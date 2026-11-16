from banner import load_banner

def render_art(text, banner_name="standard"):
    
    banner = load_banner(banner_name)
    
    text = text.replace("\\n", "\n")
    
    if text == "":
        return ""
        
    lines = text.split("\n")
    
    output_rows = []
    
    for line in lines:

        if line == "":
            output_rows.append("")
            continue
        
        for row_idx in range(8):
            current_row_str = ""
            for char in line:
                if char in banner:
                    current_row_str += banner[char][row_idx]
                else:
    
                    current_row_str += banner[" "][row_idx]
            output_rows.append(current_row_str)
                    
    return "\n".join(output_rows)