import re
import os

try:
    extract_path = "Prints_Extracted"
    files = []
    for f in os.listdir(extract_path):
        if f.startswith("Captura") and f.endswith(".png"):
            full_path = os.path.join(extract_path, f)
            files.append((f, os.path.getmtime(full_path)))
    
    files.sort(key=lambda x: x[1])
    raw_files = [x[0] for x in files]

    with open('manual_efd_contribuicoes.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
        html_imgs = re.findall(r'src=\"imagens/(.*?)\"', html_content)
    
    with open('comparison_result_utf8.txt', 'w', encoding='utf-8') as out:
        out.write(f'Total HTML references: {len(html_imgs)}\n')
        out.write(f'Total Zip files: {len(raw_files)}\n')
        out.write("--- Mapping ---\n")
        
        for i, f in enumerate(raw_files):
            if i < len(html_imgs):
                out.write(f'{i}: {f} -> {html_imgs[i]}\n')
            else:
                out.write(f'{i}: {f} -> [IGNORED/MISSING]\n')

except Exception as e:
    with open('comparison_result_utf8.txt', 'w', encoding='utf-8') as out:
        out.write(f"Error: {e}")
