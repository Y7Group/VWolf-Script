import sys
ENTER = "{ENTER}"
def convert_to_vbscript(vwolf_script, output_file):
    vbscript_code = ""
    lines = vwolf_script.split("\n")
    for line in lines:
        if line.startswith("DELAY"):
            delay = line.split(" ")[1]
            vbscript_code += "WScript.Sleep " + delay + "\n"
        elif line.startswith("STRING"):
            string = line.split(" ", 1)[1]
            vbscript_code += "x.SendKeys \"" + string + "\"\n"
        elif line.startswith("INIT"):
            vbscript_code += "Set x = CreateObject(\"WScript.Shell\")\n"
        elif line.startswith("START"):
            application = line.split(" ")[1]
            vbscript_code += "x.run " + application + "\n"
        elif line.startswith("DOWNLOAD-FILE"):
            url = line.split(" ")[1]
            outfile = line.split(" ")[2]
            vbscript_code += f'x.run "powershell"\nwscript.sleep 2000\nx.sendkeys "Invoke-WebRequest {url} -OutFile {outfile} {ENTER}"'
        # Add more conditions for other VWolfScript commands

    with open(output_file, "w") as file:
        file.write(vbscript_code)

# Example usage
if len(sys.argv) < 3:
    print("usage: <vwolf script file> <output file name>")
    sys.exit(1)

vwolf_file = sys.argv[1]
output_file = sys.argv[2] + ".vbs"

with open(vwolf_file, "r") as file:
    vwolf_script = file.read()

convert_to_vbscript(vwolf_script, output_file)
print("VBScript file generated successfully.")