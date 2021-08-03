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
				</ul>
			</li>
			<li>
				<a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=overview" target="<?php echo $link_target;?>">Indicator Groups</a>
				<ul>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=summary" target="<?php echo $link_target;?>">Summary</a></li>
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
			<li><a href="/shark/backtest/index-summary.py" target="<?php echo $link_target;?>">Summary</a>
			<ul>
				<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark/backtest/index-reports.py" target="<?php echo $link_target;?>">Reports</a></li>
				<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark/backtest/index-transactions.py" target="<?php echo $link_target;?>">Transactions</a></li>
				<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark/backtest/index-data.py" target="<?php echo $link_target;?>">Ticker Data</a></li>
			</ul>
			</li>
		</ul>
	</div>
</div>	
	
<div class="navsection">
	<div class="navsectiontitle">Strategy</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li>
				<a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=overview" target="<?php echo $link_target;?>">Strategy</a>
				<ul>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=summary" target="<?php echo $link_target;?>">Management</a></li>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/dokuwiki/doku.php" target="<?php echo $link_target;?>">Development</a></li>
				</ul>
			</li>
		</ul>
	</div>
</div>		
	
<div class="navsection">
	<div class="navsectiontitle">Configuration</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="/shark/backtest/index-summary.py" target="<?php echo $link_target;?>">Summary</a>
			<ul>
				<li><a href="/shark/backtest/index-reports.py" target="<?php echo $link_target;?>">Reports</a></li>
				<li><a href="/shark/backtest/index-transactions.py" target="<?php echo $link_target;?>">Transactions</a></li>
				<li><a href="/shark/backtest/index-data.py" target="<?php echo $link_target;?>">Ticker Data</a></li>
			</ul>
			</li>
		</ul>
	</div>
</div>	
	
</body>
</html>
