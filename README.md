# windows_tools

A simple command-line utility to run common Windows 10/11 maintenance and optimization tasks from a single menu.

## Features

- Activate/deactivate Windows 10/11
- Disable/enable Windows updates
- Disable/enable telemetry and diagnostics
- Repair missing or corrupted system files
- Disk error checking
- Disk cleanup
- Clear temporary files
- Flush DNS and reset network

![Screenshot](https://github.com/diogomcasado/windows_tools/blob/main/screenshot.PNG)

## Requirements

- Windows 10/11
- Python 3
- Dependencies: `pip install pywin32 windows-tools`

## Usage

Run the script; it will automatically request administrator privileges:

```
python windows_tools.py
```

Made for educational purposes only.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
