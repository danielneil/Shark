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
			<li><a href="https://github.com/danielneil/Shark/blob/main/README.md" target="_blank">Documentation</a></li>
		</ul>
	</div>
</div>
	
<div class="navsection">
	<div class="navsectiontitle">Instruments</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=hostdetail" target="<?php echo $link_target;?>">{{ instrument_name_plural }}</a></li>
			<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?host=all" target="<?php echo $link_target;?>">Plugins</a></li>
			<li>
				<a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=overview" target="<?php echo $link_target;?>">{{ instrument_group_name_plural }}</a>
				<ul>
					<li><a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?hostgroup=all&amp;style=summary" target="<?php echo $link_target;?>">Summary</a></li>
				</ul>
			</li>
			<li>
				<a href="<?php echo $cfg["cgi_base_url"];?>/status.cgi?servicegroup=all&amp;style=overview" target="<?php echo $link_target;?>">Plugin Groups</a>
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
	<div class="navsectiontitle">Trading</div>
	<div class="navsectionlinks">
		<ul class="navsectionlinks">
			<li><a href="#">General</a>
				<ul>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/" target="<?php echo $link_target;?>">Console</a></li>
				</ul>
			</li>
			<li><a href="#">Orders</a>
				<ul>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/" target="<?php echo $link_target;?>">Summary</a></li>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/" target="<?php echo $link_target;?>">Opened</a></li>
					<li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/" target="<?php echo $link_target;?>">Executed</a></li>
				</ul>
			</li>
		</ul>
	</div>
</div>			

<div class="navsection">
        <div class="navsectiontitle">Workbench</div>
        <div class="navsectionlinks">
                <ul class="navsectionlinks">
                        <li><a href="#">Historical Data</a>
                                <ul>
                                        <li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark/historical/" target="<?php echo $link_target;?>">Cached Data</a></li>
                                </ul>
                        </li>
                        <li><a href="#">Code</a>
                                <ul>
                                        <li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark/backtests/" target="<?php echo $link_target;?>">Backtests</a></li>
                                        <li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark/strategies/" target="<?php echo $link_target;?>">Strategies</a></li>
                                </ul>
			</li>
			<li><a href="#">Reports</a>
                                <ul>
                                        <li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/shark/reports/" target="<?php echo $link_target;?>">Backtests</a></li>
                                </ul>
                        </li>
                        <li><a href="#">Logging</a>
                                <ul>
                                        <li><a href="http://<?php echo $_SERVER['SERVER_ADDR'];?>/framework/public/app/Views/config_verification.php" target="<?php echo $link_target;?>">Config Verification</a></li>
                                </ul>
                        </li>
                </ul>
        </div>
</div>

</body>
</html>
