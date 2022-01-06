# Useful Files

Collection of some useful files, mostly for fighting spam and trolls.

## Features

`/Documents` contains some useful documents to use for different purposes  
`/mastodon blocks` contains blocklists for mastodon to keep your timeline clean  
`/Scripts` contains scripts to use, blacklist whole ASN  
`.editorconfig` Example [editorconfig](https://editorconfig.org/) file  
`.gitignore` Example gitignore file  
`.htaccess` Example htaccess file  
`20_toxic_artists.cf` Spamassassin ruleset to reject declare emails from toxic "artists" as spam  
`header_check.pcre` Postfix header check to directly reject spam declared emails from `20_toxic_artists.cf`  
`adguard_filter.txt` Filterset for AdGuard to remove the comment fields from news sites  
`archive.ip.txt` IP addresses used by archive.org, if you want to block them  
`lemmy-slur_filter.hjson` Lemmy slur filter regex to keep your [Lemmy](https://join-lemmy.org) instance clean

## Requirements

+ Mastodon Account and/or
+ Postfix installation with header checks and/or
+ Spamassassin

## Installation or Getting Started

### AdGuard Filter

Open the AdGuard settings, select Filters -> Custom -> Add custom filter  
Enter the [URL to the RAW output](https://code.bka.li/BKA.li/useful_files/raw/branch/master/adguard_filter.txt) of `adguard_filter.txt` and follow the instructions

### Mastodon blocklists

Goto settings -> Import and export -> Import  
Select the type you want to import with the dropdown and upload the file.

### Spamassassin

Place the `20_toxic_artists.cf` into `/etc/spamassassin/` and reload spamassassin

### Postfix

Copy `header_check.pcre` to `/etc/postfix/filter/` and make sure, your postfix `main.cf` contains following line:

```
header_checks = pcre:/etc/postfix/filter/header_check.pcre
```

## Contributors

Clone this project and create pull requests or create a ticket.

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)
