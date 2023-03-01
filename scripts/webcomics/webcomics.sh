day=`date "+%a"`

# AWS Discount Code:
# AVYACH28YGH7PEAL

# Daily Webcomics
#open -a "Safari" http://www.explosm.net/ | tr -d '\r'
open -a "Safari" http://questionablecontent.net/ | tr -d '\r'
open -a "Safari" http://www.egscomics.com/ | tr -d '\r'
open -a "Safari" http://www.smbc-comics.com/ | tr -d '\r'

# Monday Webcomics
if [ "$day" = "Mon" ]; then
  open -a "Safari" "http://www.grrlpowercomic.com/" | tr -d '\r'
  #open -a "Safari" "http://www.lifeinaggro.com/" | tr -d '\r'
  #open -a "Safari" "http://www.awkwardzombie.com/" | tr -d '\r'
  open -a "Safari" "http://xkcd.com/" | tr -d '\r'
  open -a "Safari" "http://www.girlgeniusonline.com/comic.php" | tr -d '\r'
  #open -a "Safari" "http://headtrip.keenspot.com/" | tr -d '\r'
  #open -a "Safari" "http://thepunchlineismachismo.com/" | tr -d '\r'
  #open -a "Safari" "http://www.collectedcurios.com/sequentialart.php" | tr -d  '\r'
  #open -a "Safari" "http://campcomic.com/comic" | tr -d '\r'
  open -a "Safari" "http://www.nexttownover.net" | tr -d '\r'
  open -a "Safari" "http://killsixbilliondemons.com/" | tr -d '\r'
  open -a "Safari" "http://www.gunnerkrigg.com/" | tr -d '\r'
  #open -a "Safari" "http://flipside.keenspot.com/" | tr -d '\r'
  open -a "Safari" "https://www.webtoons.com/en/fantasy/unordinary/list?title_no=679" | tr -d '\r'
  #open -a "Safari" "https://www.webtoons.com/en/challenge/el-bulbo-cult-hero/list?title_no=225282" | tr -d '\r'
  open -a "Safari" "http://paranatural.net/" | tr -d '\r'
  open -a "Safari" "https://www.webtoons.com/en/fantasy/suitor-armor/list?title_no=2159" | tr -d '\r'
  open -a "Safari" "https://www.webtoons.com/en/romance/lore-olympus/list?title_no=1320&page=1" | tr -d '\r'
fi

# Tuesday Webcomics
if [ "$day" = "Tue" ]; then
  open -a "Safari" "http://www.goblinscomic.com/" | tr -d '\r'
  open -a "Safari" "http://www.kiwiblitz.com/" | tr -d '\r'
  open -a "Safari" "http://www.true-magic.com/" | tr -d '\r'
  open -a "Safari" "http://falsepositivecomic.com" | tr -d '\r'
  open -a "Safari" "http://www.powernapcomic.com/" | tr -d '\r'
  open -a "Safari" "http://www.sleeplessdomain.com" | tr -d '\r'
  open -a "Safari" "http://www.demonstreet.co/" | tr -d '\r'
fi

# Wednesday Webcomics
if [ "$day" = "Wed" ]; then
  open -a "Safari" "http://xkcd.com/"  | tr -d '\r'
  open -a "Safari" "http://girlgeniusonline.com/comic.php" | tr -d '\r'
  #open -a "Safari" "http://northwindcomic.com" | tr -d '\r'
  open -a "Safari" "http://killsixbilliondemons.com/" | tr -d '\r'
  open -a "Safari" "http://www.gunnerkrigg.com/" | tr -d '\r'
  #open -a "Safari" "http://flipside.keenspot.com" | tr -d '\r'
fi

# Thursday Webcomics
if [ "$day" = "Thu" ]; then
  open -a "Safari" "http://www.kiwiblitz.com/" | tr -d '\r'
  #open "http://campcomic.com/comic"
  open -a "Safari" "http://falsepositivecomic.com" | tr -d '\r'
  open -a "Safari" "http://www.grrlpowercomic.com/" | tr -d '\r'
  open -a "Safari" "http://www.sleeplessdomain.com" | tr -d '\r'
fi

# Friday Webcomics
if [ "$day" = "Fri" ]; then
  open -a "Safari" "http://xkcd.com/" | tr -d '\r'
  open -a "Safari" "http://www.goblinscomic.com/" | tr -d '\r'
  open -a "Safari" "http://www.girlgeniusonline.com/comic.php" | tr -d '\r'
  open -a "Safari" "http://killsixbilliondemons.com/" | tr -d '\r'
  open -a "Safari" "http://www.gunnerkrigg.com/" | tr -d '\r'
  #open -a "Safari" "http://flipside.keenspot.com/" | tr -d '\r'
fi

#REM Inactive Webcomics
#IF %DATE:~0,3% == Mon start chrome.exe "http://makeshiftmiracle.keenspot.com/"
#  open -a "Safari" "http://medusa.keenspot.com/" | tr -d '\r'
#http://www.turbodefiant.com/webcomic_eng/2/tdk091.php
  #open -a "Safari" "http://www.avasdemon.com/" | tr -d '\r'
  #open -a "Safari" "http://www.amazingsuperpowers.com/"
  #open "http://bearmageddon.com/"
  #open -a "Safari" "http://vioectrolysis.dreamwidth.org/" | tr -d '\r'
  #open -a "Safari" "http://shiverbureau.com/" | tr -d '\r'
  #open -a "Safari" "http://monsterkind.enenkay.com" | tr -d '\r'

#REM Not Caught Up
#start chrome.exe "http://www.menagea3.net/"
#start chrome.exe "http://mysticrevolution.keenspot.com/"
#start chrome.exe "http://www.widdershinscomic.com/"
  #open "http://www.metacarpolis.com/"
  #open "http://www.endcomic.com/"
  #open "http://trenchescomic.com/"
  #open -a "Safari" "http://flakypastry.runningwithpencils.com/" | tr -d '\r'
  #open -a "Safari" "http://www.speakdevil.com/" | tr -d  '\r'

#REM Concluded comics, but not read

#REM Concluded comics, kept for records
#https://tapas.io/trbledmind
#open -a "Safari" "http://www.sandraandwoo.com/gaia/" | tr -d '\r'
#open -a "Safari" http://www.sssscomic.com/comic.php | tr -d '\r'
#open -a "Safari" "http://www.monster-pulse.com" | tr -d '\r'
#open -a "Safari" "http://www.starpowercomic.com/" | tr -d '\r'
#open -a "Safari" "http://www.supernormalstep.com" | tr -d '\r'
#open -a "Safari" "http://drmcninja.com/" | tr -d '\r'
#open "http://brawlinthefamily.keenspot.com/"
#open -a "Safari" "http://gingerhaze.com/nimona"
#start chrome.exe "http://darkencomic.com/"
#open -a "Safari" http://www.girlswithslingshots.com/ | tr -d '\r'
#zap in space
#open -a "Safari" "http://skullkickers.keenspot.com/" | tr -d '\r'
#https://parahumans.wordpress.com
#http://www.mangareader.net/gantz

#BOOKMARKS
#http://flipside.keenspot.com/comic.php?i=3341

#REM To be added
  #open "http://www.penny-arcade.com/"
#http://www.casualvillain.com/Unsounded/comic/ch01/ch01_01.html
#http://thrillbent.com/comics/insufferable/
#http://strongfemaleprotagonist.com/
#pictures of you
#a girl and her fed -- http://agirlandherfed.com/1.875.html
#rom.ac
#head trip
#holiday wars
#dreamland chronicles
#http://www.asofterworld.com/
#buttersafe
#rock paper cynic
#misfile
#http://cloudfactorycomics.tumblr.com/
#http://phuzzycomics.monicaray.com/comic/guan-why/
#http://sci-ence.org/entropy/
#rare candy treatment
#clcomic.com/?latest

# Abandoned Webcomics
#open -a "Safari" "http://broodhollow.chainsawsuit.com/" | tr -d '\r'
#open "http://www.olympusoverdrive.com/"
#start chrome.exe "http://www.finderskeepers.gcgstudios.com/"
# Emergency exit
  #open -a "Safari" "http://runewriters.com/" | tr -d '\r'
  #open -a "Safari" "http://www.proteansea.com/" | tr -d '\r'


#Manga & Other Stuff
#http://www.mangareader.net/bloody-monday
#http://www.mangareader.net/deadman-wonderland
#http://www.mangareader.net/akame-ga-kiru
#https://pactwebserial.wordpress.com/2013/12/17/bonds-1-1/
#https://twigserial.wordpress.com/2014/12/24/taking-root-1-1/
#http://www.mangareader.net/jojos-bizarre-adventure-part-4-diamond-is-unbreakable/12/95

