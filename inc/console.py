#!/usr/bin/env python
# coding=utf-8
  ################
 #   AabyssZG   #
################

from inc import output,run,vul,springcheck,zoom,fofa,poc,hunter
import sys,asyncio,re

# 控制台-参数处理和程序调用
async def SpringBoot_Scan_console(args, proxies,header_new):

    if args.url:
        urlnew = await springcheck.check(args.url, proxies,header_new)
        await run.async_url(urlnew, proxies,header_new)
    if args.urlfile:
        asyncio.run(run.file_main(args.urlfile,proxies,header_new))
    if args.vul or args.vulfile or args.dump or args.zoomeye or args.fofa or args.hunter:
        proxy=get_proxy(proxies)
        if args.vul:
            urlnew = await springcheck.check(args.vul,proxies ,header_new)
            vul.vul(urlnew, proxy,header_new)
        if args.vulfile:
            poc.poc(args.vulfile, proxy)
        if args.dump:
            urlnew = await springcheck.check(args.dump, proxies,header_new)
            run.dump(urlnew, proxy,header_new)
        if args.zoomeye:
            zoom.ZoomDowload(args.zoomeye,proxy)
        if args.fofa:
            fofa.FofaDowload(args.fofa,proxy)
        if args.hunter:
            hunter.HunterDowload(args.hunter,proxy)
        else:
            output.usage()
            sys.exit()

def get_proxy(proxys):
    pattern = r"(http|https|socks4|socks5)://([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}:[\d]{1,5})"
    match = re.search(pattern, proxys)
    proxy = {match.group(1):match.group(2)}
    return proxy
