import subprocess
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

# Set locale to US English so output matches the expected strings
env = {"LC_ALL": "en_US.utf8"}

# Function to run a command with pkexec
def run_with_pkexec(cmd):
    return subprocess.check_output(['pkexec', 'sh', '-c', cmd], env=env)

# Run the commands and store their output in variables
bios_info = run_with_pkexec("dmidecode | grep -A3 'Vendor:'")
cpu_info = subprocess.check_output("lshw -C cpu | grep -A3 'product:'", shell=True, env=env)
kernel_version = subprocess.check_output("uname -r", shell=True, env=env)

# Create a GTK dialog window with larger text and a bigger size
dialog = Gtk.MessageDialog(parent=None, flags=0, message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.OK, text="Framework System Details")
dialog.set_markup("<span size='xx-large' weight='bold'>BIOS Information:</span>\n{}\n<span size='xx-large' weight='bold'>CPU Information:</span>\n{}\n<span size='xx-large' weight='bold'>Kernel Version:</span> {}".format(bios_info.decode(), cpu_info.decode(), kernel_version.decode()))
dialog.format_secondary_markup(None)
dialog.set_size_request(600, 400)
dialog.run()
dialog.destroy()

