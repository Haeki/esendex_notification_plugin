# Notification Plugin for SMS delivery via esendex.com

This is a check_mk notification plugin to send sms messages via <a href="https://www.esendex.com">esendex</a>.
<p> You need a paid account at their service and your user name, api password and account reference for the configuration of this notification method. <p>

Version 2.x supports message bulking

Optional Parameters:
<ul>
  <li> SMS Header: will be added to the start of each message</li>
  <li> Service output sub pattern: Regex-pattern. All matches will get cut from the service output. Default "WARN - |CRIT - |OK -" to remove duplicated status.</li>
  <li> Max Message Lenght: Max Number of characters the final message will have. Service outputs will be cut first to save space, if the message is still to long the message will get truncated </li>
</ul>


The code started based on: https://github.com/HeinleinSupport/check_mk_extensions/tree/master/notifications/aspsms
