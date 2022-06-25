<!--
title: "Postfix mail delivery delay monitoring with Netdata"
custom_edit_url: https://github.com/netdata/netdata/edit/master/collectors/python.d.plugin/postfix_delay/README.md
sidebar_label: "Postfix Delivery Delay"
-->

# Postfix delivery delay monitoring with Netdata

Monitors MTA email delay statistics using mailogs.  

Parses the mail log `/var/log/maillog` to grab delivery delay stats.

It produces only one charts:

1.  **Postfix Average Mail Delay**

    -   seconds

## Requirements

The `/var/log/maillog` file must be readable by the user `netdata`.

## Configuration

Edit the `python.d/postfix_delay.conf` configuration file to change the log file path.
Netdata must have permission to read the file.
---


