# Useful Files

Collection of some useful files, mostly for fighting spam and trolls.

## Features

`/Documents` contains some useful documents to use for different purposes  
`/Mastodon blocks` contains blocklists for mastodon to keep your timeline clean  
`/Scripts` contains scripts to use, in example the script to block whole ASN via iptables  
`.editorconfig` Example [editorconfig](https://editorconfig.org/) file  
`.gitignore` Example gitignore file  
`.htaccess` Example htaccess file  
`20_toxic_artists.cf` Spamassassin ruleset to add points to toxic "artists" and declare them as spam  
`header_check.pcre` Postfix header check to directly reject as spam declared emails from `20_toxic_artists.cf`  
`adguard_filter.txt` Filterset for AdGuard to remove the comment fields from news sites. We want newsand not unqualified comments  
`archive.ip.txt` IP addresses used by archive.org and archive.is, if you want to block them  
`lemmy-slur_filter.hjson` Lemmy slur filter regex to keep your [Lemmy](https://join-lemmy.org) instance clean. Used on [fapsi.be](https://fapsi.be)

## Requirements

+ Mastodon account and/or
+ Postfix installation with header checks and/or
+ Spamassassin

## Installation

### AdGuard Filter

Open the AdGuard settings, select Filters -> Custom -> Add custom filter  
Enter the [URL to the RAW output](https://code.bka.li/BKA.li/useful_files/raw/branch/master/adguard_filter.txt) of `adguard_filter.txt` and follow the instructions

### Mastodon blocklists

Goto Settings -> Import and export -> Import  
Select the type you want to import with the dropdown and upload the file.

### Spamassassin

Copy `20_toxic_artists.cf` to `/etc/spamassassin/` and reload spamassassin

### Postfix

Copy `header_check.pcre` to `/etc/postfix/filter/` and make sure, your postfix `main.cf` contains following line:

```
header_checks = pcre:/etc/postfix/filter/header_check.pcre
```

## Contributors

[Fork this project](https://code.bka.li/repo/fork/19) and create pull requests or create [an issue](https://code.bka.li/BKA.li/useful_files/issues).

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)
