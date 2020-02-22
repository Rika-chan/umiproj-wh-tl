import re
import sys
import glob
import os

ep = sys.argv[1]
search_re = re.compile(r"@|~|!\w|#")
fixes = {}
if os.path.isfile(ep):
    file_expr = ep
else:
    file_expr = f"{ep}/wh/*.txt"
for tled_file in glob.glob(file_expr):
    try:
        fixes[os.path.basename(tled_file)] = {}
        tled_lines = open(tled_file, encoding="utf-8").readlines()
        parent_dir = os.path.dirname(os.path.dirname(tled_file))
        original_lines = open(
            f"{parent_dir}/en/{os.path.basename(tled_file)}", encoding="utf-8"
        ).readlines()
        if len(original_lines) != len(tled_lines):
            print(f"Line counts don't match for {tled_file}, giving up.")
            sys.exit()
        for i, line in enumerate(tled_lines):
            if search_re.search(line) is not None:
                fixes[os.path.basename(tled_file)][i] = (line, original_lines[i])
    except:
        print(f"Error in file {tled_file}, stopping.")
        raise
if not os.path.exists("script_fixup.txt"):
    ffile = open("script_fixup.txt", "w", encoding="utf-8")
    for filename, lines in fixes.items():
        for line_number, line in lines.items():
            print(
                f"{filename}:{line_number}: {line[0].strip()} -> {line[1].strip()}",
                file=ffile,
            )
    print("Please edit script_fixup.txt and adjust the needed fixes.")
else:
    print("Fixing lines from script_fixup.txt...")
    fix_lines = open("script_fixup.txt", encoding="utf-8").readlines()
    fixes_applied = [x.split(":", 2) for x in fix_lines]
    for fix in fixes_applied:
        try:
            tled_lines = open(f"{ep}/wh/{fix[0]}", encoding="utf-8").readlines()
            try:
                fixes[fix[0]][int(fix[1])]
            except:
                print(
                    f"{fix[0]}:{fix[1]} doesn't need fixing but is in fixes list, skipping."
                )
                continue
            tled_lines[int(fix[1])] = fix[2].split("->", 1)[1].strip() + "\n"
            open(f"{ep}/wh/{fix[0]}", "w", encoding="utf-8").writelines(tled_lines)
        except:
            pass
    os.remove("script_fixup.txt")
    print("Adjusting spaces...")
    for tled_file in glob.glob(file_expr):
        lines = open(tled_file, encoding="utf-8").readlines()
        lines = [re.sub(r"\s*`$", " `", re.sub(r"^`\s+", "`", x)) for x in lines]
        open(tled_file, "w", encoding="utf-8").writelines(lines)
