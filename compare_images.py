import re
import os

try:
    with open('sorted_prints.txt', 'r', encoding='utf-16-le') as f:
        # Skip header lines, find lines starting with 'Captura'
        raw_files = []
        for line in f:
            parts = line.strip().split()
            if len(parts) > 0 and parts[0] == 'Captura':
                # Reconstruct filename "Captura de tela..."
                # In powershell output, Name is first. BUT it might be truncated in the txt if not careful?
                # Actually, Select-Object Name gets the whole name.
                # Let's assume the line starts with the name. 
                # But wait, the file has Name and LastWriteTime.
                # Example: Captura de tela 2024-01-29 1430.png 29/01/2026 14:30:00
                # Let's simple take the whole line until the date part?
                # Or just list dir properly.
                pass
    
    # Let's try listing the directory directly in python to be safer
    files = []
    extract_path = "Prints_Extracted"
    for f in os.listdir(extract_path):
        if f.startswith("Captura") and f.endswith(".png"):
            full_path = os.path.join(extract_path, f)
            files.append((f, os.path.getmtime(full_path)))
    
    # Sort by time
    files.sort(key=lambda x: x[1])
    raw_files = [x[0] for x in files]

    with open('manual_efd_contribuicoes.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
        html_imgs = re.findall(r'src=\"imagens/(.*?)\"', html_content)
    
    print(f'Total HTML references: {len(html_imgs)}')
    print(f'Total Zip files: {len(raw_files)}')

    print("--- Mapping ---")
    for i, f in enumerate(raw_files):
        if i < len(html_imgs):
            print(f'{i}: {f} -> {html_imgs[i]}')
        else:
            print(f'{i}: {f} -> [IGNORED/MISSING]')

except Exception as e:
    print(f"Error: {e}")
