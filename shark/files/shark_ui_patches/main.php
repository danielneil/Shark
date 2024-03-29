<?php
include_once(dirname(__FILE__).'/includes/utils.inc.php');

$this_version = '4.4.6';
$this_year = '2020';
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<html>

<head>

<meta name="ROBOTS" content="NOINDEX, NOFOLLOW" />
<title>Algorithmic Trading Platform</title>
<link rel="stylesheet" type="text/css" href="stylesheets/common.css?<?php echo $this_version; ?>" />
<link rel="stylesheet" type="text/css" href="stylesheets/nag_funcs.css?<?php echo $this_version; ?>" />
<script type="text/javascript" src="js/jquery-1.12.4.min.js"></script>
<script type="text/javascript" src="js/nag_funcs.js"></script>

<script type='text/javascript'>
	var cookie;
	<?php if ($cfg["enable_page_tour"]) { ?>
		var vbox;
		var vBoxId = "main";
		var vboxText = "<a href=https://www.nagios.com/tours target=_blank> " +
						"Click here to watch the entire Nagios Core 4 Tour!</a>";

	<?php } ?>
	$(document).ready(function() {
		var user = "<?php echo htmlspecialchars($_SERVER['REMOTE_USER']); ?>";

		loadRemoteFeed( // Our top banner splash.
			'#splashbox0-contents', 'corebanner', 1,
			'', processBannerItem, ''
		);

		loadRemoteFeed( // "Latest News"
			'#splashbox4-contents', 'frontpage', 3,
			'<ul>', processNewsItem, '<li><a href="https://www.nagios.org/news" target="_blank">More news...</a></li></ul>'
		);

		loadRemoteFeed( // "Don't Miss..."
			'#splashbox5-contents', 'corepromo', 3,
			'<ul>', processPromoItem, '</ul>'
		);

		getCoreStatus();
	});

	// Fetch an RSS feed and format HTML for the first n items.
	function loadRemoteFeed(id, name, n, prefix, formatter, suffix) {
		$.ajax({
			type: 'GET',
			url: 'https://www.nagios.org/backend/feeds/' + name + '/',
			crossDomain: true,
			success: function(d, status, jqXHR) {
				// We should have Internet access, set the playlist HTML.
				initializePlaylist();

				var text = ''; // Start with empty text by default.

				$(d).find('channel').find('item').each(function(index) {
					var itemText = formatter($(this)); // Format the item's HTML.
					if (itemText) text += itemText; // Append if non-empty.
					return index+1 < n; // Only process n items.
				});

				// Only set the HTML if we have item text.
				if (text) $(id).html(prefix + text + suffix);
			}
		});
	}

	function processBannerItem(item) {
		return item.find('description').text();
	}

	function processNewsItem(item) {
		var link = item.find('link').text();
		var title = item.find('title').text();
		return link && title
			? '<li><a href="' + link + '" target="_blank">' + title + '</a></li>'
			: '';
	}

	function processPromoItem(item) {
		var description = item.find('description').text();
		return description
			? '<li>' + description + '</li>'
			: '';
	}

	// Set our playlist HTML when we know we have Internet access.
	var playlistInitialized = false;
	function initializePlaylist() {
			$('#splashbox3')
				.addClass('splashbox3-full')
				.removeClass('splashbox3-empty')
				.html('<iframe width="100%" height="100%" src="https://www.youtube.com/watch?v=OPm_EDTrz7Y" frameborder="0" allowfullscreen></iframe>');
		}


	// Get the daemon status JSON.
	function getCoreStatus() {
		setCoreStatusHTML('passiveonly', 'Checking process status...');

		$.get('<?php echo $cfg["cgi_base_url"];?>/statusjson.cgi?query=programstatus', function(d) {
			d = d && d.data && d.data.programstatus || false;
			if (d && d.nagios_pid) {
				var pid = d.nagios_pid;
				var daemon = d.daemon_mode ? 'Daemon' : 'Process';
				setCoreStatusHTML('enabled', daemon + ' running with PID ' + pid);
			} else {
				setCoreStatusHTML('disabled', 'Not running');
			}
		}).fail(function() {
			setCoreStatusHTML('disabled', 'Unable to get process status');
		});
	}

	function setCoreStatusHTML(image, text) {
		$('#core-status').html('<img src="images/' + image + '.gif" /> ' + text);
	}
</script>

</head>


<body id="splashpage">


<div id="mainbrandsplash">
	<div id="mainlogo"><a href="https://www.github.com/danielneil/Shark/" target="_blank"><img src="images/logofullsize.png" border="0" alt="Shark" title="Shark"></a></div>
	<div><span id="core-status"></span></div>
</div>


<div id="currentversioninfo">
	<div class="product">Shark<sup><span style="font-size: small;">&reg;</span></sup> Algorithmic Trading Platform<sup><span style="font-size: small;">&trade;</span></sup></div>
	<div class="version">Version <?php echo $this_version; ?></div>
	<div class="releasedate">April 28, 2020</div>
	<div class="checkforupdates"><a href="https://www.github.com/danielneil/Shark" target="_blank">Github</a></div>
</div>


<div id="updateversioninfo">
<?php
	$updateinfo = get_update_information();
	if (!$updateinfo['update_checks_enabled']) {
?>
		<div class="updatechecksdisabled">
			<div class="warningmessage">Warning: Automatic Update Checks are Disabled!</div>
			<div class="submessage">Disabling update checks presents a possible security risk.  Visit <a href="https://www.nagios.org/" target="_blank">nagios.org</a> to check for updates manually or enable update checks in your Nagios config file.</a></div>
		</div>
<?php
	} else if (
		$updateinfo['update_available'] && $this_version < $updateinfo['update_version']
	) {
?>
		<div class="updateavailable">
			<div class="updatemessage">A new version of Nagios Core is available!</div>
			<div class="submessage">Visit <a href="https://www.nagios.org/download/" target="_blank">nagios.org</a> to download Nagios <?php echo $updateinfo['update_version'];?>.</div>
		</div>
<?php
	}
?>
</div>



	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

<div id="mainfooter">
	<div CLASS="disclaimer">
		Shark is licensed under the GNU General Public License and is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE WARRANTY OF DESIGN, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.  
		<br />
		<br />
		Trading Futures, Forex, CFDs, Cryptocurrencies and Stocks involves a risk of loss. Please consider carefully if such trading is appropriate for you. Past performance is not indicative of future results. Information and content in and derived from this application are for entertainment purposes only and do not constitute investment recommendations or advice.
	</div>
	<div class="logos">
		<a href="https://www.nagios.org/" target="_blank"><img src="images/weblogo1.png" width="102" height="47" border="0" style="padding: 0 40px 0 40px;" title="Nagios.org" /></a>
		<a href="http://sourceforge.net/projects/nagios" target="_blank"><img src="images/sflogo.png" width="88" height="31" border="0" alt="SourceForge.net Logo" /></a>
	</div>
</div>


</body>
</html>
