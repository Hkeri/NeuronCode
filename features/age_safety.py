import time
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def age_safety(yesorno: str):
    if is_admin():
        host_path ='C:\Windows\System32\drivers\etc\hosts'
        redirect = '127.0.0.1'
        time.sleep(2)
        website_list = [
        "www.pornhub.com",
        "pornhub.com",
        "www.xhamster.com",
        "xhamster.com",
        "www.xvideos.com",
        "xvideos.com",
        "www.onlyfans.com",
        "onlyfans.com",
        "www.youporn.com",
        "youporn.com",
        "www.bellessa.com",
        "bellessa.com",
        "www.XNXX.com",
        "XNXX.com",
        "www.adultchat.net",
        "www.flingster.com",
        "www.chat-avenue.com",
        "www.chatville.com",
        "www.chatropolis.com",
        "www.321sexchat.com",
        "adultfriendfinder.com",
        "www.bangsexting.com",
        "www.benaughty.com",
        "www.sextfriend.com",
        "www.arousr.chat",
        "www.kikfriender.com",
        "www.adultchat.net",
        "www.flingster.com",
        "www.chat-avenue.com",
        "www.chatville.com",
        "www.chatropolis.com",
        "www.321sexchat.com",
        "adultfriendfinder.com",
        "www.bangsexting.com",
        "www.benaughty.com",
        "www.sextfriend.com",
        "www.arousr.chat",
        "www.kikfriender.com",
        "tinder.com",
        "match.com",
        "pof.com",
        "datehookup.dating",
        "okcupid.com",
        "eharmony.com",
        "omegle.com",
        "9gag.com",
        "www.tinder.com",
        "www.match.com",
        "www.pof.com",
        "www.datehookup.dating",
        "www.okcupid.com",
        "www.eharmony.com",
        "www.omegle.com",
        "www.9gag.com",
        "www.bet365.com",
        "www.betano.com",
        "www.sportybet.com",
        "www.betfair.com",
        "www.covers.com",
        "www.fanduel.com",
        "bet365.com",
        "betano.com",
        "sportybet.com",
        "betfair.com",
        "covers.com",
        "fanduel.com",
        "documentingreality.com",
        "livegore.com",
        "xgore.net",
        "gorecenter.com",
        "screamer.wiki",
        "4chan.org",
        "www.documentingreality.com",
        "www.livegore.com",
        "www.xgore.net",
        "www.gorecenter.com",
        "www.screamer.wiki",
        "www.4chan.org",
        "www.piratebay.com",
        "www.darkweblinks.net",
        "www.wikileaks.org",
        "www.hackthissite.org",
        "piratebay.com",
        "darkweblinks.net",
        "wikileaks.org",
        "hackthissite.org"
        ]
        if yesorno == "N":
            with open(host_path,"r+") as file: #r+ is writing+ reading
                content = file.read()
                time.sleep(2)
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        file.write(f"{redirect} {website}\n")
                        time.sleep(1)
        while True:
            website_list = [
        "www.pornhub.com",
        "pornhub.com",
        "www.xhamster.com",
        "xhamster.com",
        "www.xvideos.com",
        "xvideos.com",
        "www.onlyfans.com",
        "onlyfans.com",
        "www.youporn.com",
        "youporn.com",
        "www.bellessa.com",
        "bellessa.com",
        "www.XNXX.com",
        "XNXX.com",
        "www.adultchat.net",
        "www.flingster.com",
        "www.chat-avenue.com",
        "www.chatville.com",
        "www.chatropolis.com",
        "www.321sexchat.com",
        "adultfriendfinder.com",
        "www.bangsexting.com",
        "www.benaughty.com",
        "www.sextfriend.com",
        "www.arousr.chat",
        "www.kikfriender.com",
        "www.adultchat.net",
        "www.flingster.com",
        "www.chat-avenue.com",
        "www.chatville.com",
        "www.chatropolis.com",
        "www.321sexchat.com",
        "adultfriendfinder.com",
        "www.bangsexting.com",
        "www.benaughty.com",
        "www.sextfriend.com",
        "www.arousr.chat",
        "www.kikfriender.com",
        "tinder.com",
        "match.com",
        "pof.com",
        "datehookup.dating",
        "okcupid.com",
        "eharmony.com",
        "omegle.com",
        "9gag.com",
        "www.tinder.com",
        "www.match.com",
        "www.pof.com",
        "www.datehookup.dating",
        "www.okcupid.com",
        "www.eharmony.com",
        "www.omegle.com",
        "www.9gag.com",
        "www.bet365.com",
        "www.betano.com",
        "www.sportybet.com",
        "www.betfair.com",
        "www.covers.com",
        "www.fanduel.com",
        "bet365.com",
        "betano.com",
        "sportybet.com",
        "betfair.com",
        "covers.com",
        "fanduel.com",
        "documentingreality.com",
        "livegore.com",
        "xgore.net",
        "gorecenter.com",
        "screamer.wiki",
        "4chan.org",
        "www.documentingreality.com",
        "www.livegore.com",
        "www.xgore.net",
        "www.gorecenter.com",
        "www.screamer.wiki",
        "www.4chan.org",
        "www.piratebay.com",
        "www.darkweblinks.net",
        "www.wikileaks.org",
        "www.hackthissite.org",
        "piratebay.com",
        "darkweblinks.net",
        "wikileaks.org",
        "hackthissite.org"
        ]
            if yesorno == "Y":
                with open(host_path,"r+") as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    file.truncate()
                    
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)