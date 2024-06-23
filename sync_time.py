import ntplib
import subprocess
import platform
import time
class Synchronize_time: 
  def synchronize():
    try:
      client = ntplib.NTPClient()
      response = client.request('pool.ntp.org', version=3)  # Use NTPv3 for better security
      # Calculate time offset and handle potential rounding errors
      time_offset = response.tx_time - time.time()
      if abs(time_offset) > 1:  # Allow for a maximum 1-second offset before adjusting
        if platform.system() == 'Windows':
          subprocess.run(['w32tm', '/resync'], check=True)
          return "Synchronizing time on Windows..."
        elif platform.system() == 'Linux':
          subprocess.run(['sudo', 'ntpdate', '-u', 'pool.ntp.org'], check=True)
          return "Synchronizing time on Linux..."
        else:
          return f"Unsupported operating system: {platform.system()}"

      else:
        return "Time is already synchronized."

    except ntplib.NTPException as e:
      return f"NTP error: {e}"
    except subprocess.CalledProcessError as e:
      return f"Error synchronizing time: {e}"
