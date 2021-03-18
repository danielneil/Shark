<?php
include_once(dirname(__FILE__).'/includes/utils.inc.php');

$this_version = '4.4.6';
$link_target = 'main';
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<html>

<head>
<meta name="ROBOTS" content="NOINDEX, NOFOLLOW">
<title>Algorithmic Trading Platform</title>
<link href="stylesheets/common.css?<?php echo $this_version; ?>" type="text/css" rel="stylesheet">
</head>


<body class='navbar'>

<div class="navbarlogo">
	<a href="https://www.github.com/danielneil/Shark" target="_blank"><img src="images/sblogo.png" height="39" width="140" border="0" alt="Be a shark" /></a>
</div>

<div class="navsection">
	<div class="navsectiontitle">General</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="main.php" target="<?php echo $link_target;?>">Home</a></li>
			<li><a href="https://github.com/danielneil/Shark/tree/main/doc" target="_blank">Documentation</a></li>
		</ul>
	</div>
</div>

<div class="navsection">
	<div class="navsectiontitle">Current Status</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=hostdetail" target="<?php echo $link_target;?>">Stocks</a></li>
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?host=all" target="<?php echo $link_target;?>">Indicators</a></li>
			<li>
				<a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=overview" target="<?php echo $link_target;?>">Industry Groups</a>
				<ul>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=summary" target="<?php echo $link_target;?>">Summary</a></li>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=grid" target="<?php echo $link_target;?>">Grid</a></li>
				</ul>
			</li>
			<li>
				<a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=overview" target="<?php echo $link_target;?>">Indicator Groups</a>
				<ul>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=summary" target="<?php echo $link_target;?>">Summary</a></li>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=grid" target="<?php echo $link_target;?>">Grid</a></li>
				</ul>
			</li>
		</ul>
	</div>
	<div class="navbarsearch">
		<form method="get" action="<?php echo $cfg["cgi_base_url"];?>/status.cgi" target="<?php echo $link_target;?>">
			<fieldset>
				<legend>Ticker Search:</legend>
				<input type='hidden' name='navbarsearch' value='1'>
				<input type='text' name='host' size='15' class="NavBarSearchItem">
			</fieldset>
		</form>
	</div>
</div>
	
<div class="navsection">
	<div class="navsectiontitle">Backtesting</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="/shark/backtest" target="<?php echo $link_target;?>">Summary</a>
			<ul>
				<li><a href="/shark/backtest/index.php?action=reports" target="<?php echo $link_target;?>">Reports</a></li>
				<li><a href="/shark/backtest/index.php?action=transactions" target="<?php echo $link_target;?>">Trade Logs</a></li>
			</ul>
			</li>
		</ul>
	</div>
</div>	
	
<div class="navsection">
	<div class="navsectiontitle">Reports</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/avail.cgi" target="<?php echo $link_target;?>">Availability</a></li>
			<li>
				<a href="trends.html" target="<?php echo $link_target;?>">Trends</a>
				<a href="<?php echo $cfg["cgi_base_url"];?>/trends.cgi" target="<?php echo $link_target;?>">(Legacy)</a>
			</li>
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/history.cgi?host=all" target="<?php echo $link_target;?>">Alerts</a>
			<ul>
				<li><a href="<?php echo $cfg["cgi_base_url"];?>/history.cgi?host=all" target="<?php echo $link_target;?>">History</a></li>
				<li><a href="<?php echo $cfg["cgi_base_url"];?>/summary.cgi" target="<?php echo $link_target;?>">Summary</a></li>
				<li>
					<a href="histogram.html" target="<?php echo $link_target;?>">Histogram</a>
					<a href="<?php echo $cfg["cgi_base_url"];?>/histogram.cgi" target="<?php echo $link_target;?>">(Legacy)</a>
				</li>
			</ul>
			</li>
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/notifications.cgi?contact=all" target="<?php echo $link_target;?>">Notifications</a></li>
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/showlog.cgi" target="<?php echo $link_target;?>">Event Log</a></li>
		</ul>
	</div>
</div>
	
<div class="navsection">
	<div class="navsectiontitle" style="background-color: red; color: white; text-align: center">Development</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:15672" target="_blank">RabbitMQ WebUI</a></li>
			<li><a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:8047" target="_blank">Apache Drill WebUI</a></li>
			<li><a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>/shark" target="_blank">Work Directory</a></li>
			<li><a href="http://<?php echo $_SERVER['SERVER_ADDR']; ?>:81" target="_blank">Arch Monitoring</a></li>
		</ul>
	</div>
</div>

</body>
</html>
