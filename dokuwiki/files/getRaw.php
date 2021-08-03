<?php
if(!defined('DOKU_INC')) define('DOKU_INC', dirname(__FILE__).'/');
require_once(DOKU_INC.'inc/init.php');
 
$ID = cleanID(getID());
$onlyCode = $INPUT->str('onlyCode');
$insideTag = $INPUT->str('insideTag');
 
if (empty($conf['useacl']) || auth_quickaclcheck($ID) >= AUTH_READ) {
	$file = rawWiki($ID);
	if ($onlyCode)
		$file = preg_replace('/[\s\S]*<code( \w>|>)/m', '', preg_replace('/<\/code>[\s\S]*/m', '', $file));
	if ($insideTag)
		$file = preg_replace('/[\s\S]*<' . $insideTag . '[^>]*>/m', '', preg_replace('/<\/' . $insideTag . '>[\s\S]*/m', '', $file));
	print $file;
}
else
	print "Unauthorized";
?>
