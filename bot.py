

import discord
from discord.ext import commands
import asyncio
import random
import logging
import token
import time
import os
import sys

command_prefix = "v." #CHANGE IT TO WHAT YOU WANT
bot = commands.Bot(command_prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')

###################################
############## Events #############
###################################

@bot.event
async def on_command_error(error,ctx):
    channel=ctx.message.channel
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        if ctx.invoked_subcommand:
            pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                em = discord.Embed(description=":x: **Error ~ Missing Input** • `"+page.strip("```").replace('<', '[').replace('>', ']')+"`",
                                color=discord.Color.blue())
                await bot.send_message(ctx.message.channel, embed=em)
        else:
            pages = bot.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                em = discord.Embed(description=":x: **Error ~ Missing Input** • `"+page.strip("```").replace('<', '[').replace('>', ']')+"`",
                                color=0x003f80)
                await bot.send_message(ctx.message.channel, embed=em)
                return
    elif isinstance(error, commands.BadArgument):
        if ctx.invoked_subcommand:
            pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
            for page in pages:
                em = discord.Embed(description=":x: **Error ~ Invalid Input** • `"+page.strip("```").replace('<', '[').replace('>', ']')+"`",
                                color=discord.Color.blue())
                await bot.send_message(ctx.message.channel, embed=em)
        else:
            pages = bot.formatter.format_help_for(ctx, ctx.command)
            for page in pages:
                em = discord.Embed(description=":x: **Error ~ Invalid Input** • `"+page.strip("```").replace('<', '[').replace('>', ']')+"`",
                                color=0x003f80)
                await bot.send_message(ctx.message.channel, embed=em)
                return
    elif isinstance(error, commands.CommandInvokeError):
        print("Error  >  Exception in command '{}', {}".format(ctx.command.qualified_name, error.original))

###################################
############# Commands ############
###################################

@bot.event
async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            em = discord.Embed(description=page.strip("```").replace('<', '[').replace('>', ']'),
                               color=discord.Color.blue())
            await bot.send_message(ctx.message.channel, embed=em)
    else:
        pages = bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            em = discord.Embed(description=page.strip("```").replace('<', '[').replace('>', ']'),
                               color=0x003f80)
            await bot.send_message(ctx.message.channel, embed=em)
            return

###################################

@bot.command(pass_context=True)
async def createroles(ctx):
    serverroles=ctx.message.server.roles
    author=ctx.message.author
    authorr = '337309362575900672'
    if "Venus Mod" in [x.name for x in serverroles]:
            embed = discord.Embed(description = ":x: Roles already **Exist**", color = 0x003f80)
            return await bot.say(embed = embed)
    if "Venus Muted" in [x.name for x in serverroles]:
            embed = discord.Embed(description = ":x: Roles already **Exist**", color = 0x003f80)
            return await bot.say(embed = embed)
    else:
        if author.server_permissions.administrator:
            try:
                permissions = discord.Permissions(send_messages = False)
                await bot.create_role(ctx.message.server,name="Venus Mod")
                await bot.create_role(ctx.message.server,name="Venus Muted", permissions=permissions)
                embed = discord.Embed(description = "**:white_check_mark: Roles For Commands Created!**", color = 0xcd6800)
                return await bot.say(embed = embed)
                await bot.say(embed=embed)
            except Exception as e:
                print(e)
                if str(e) == "FORBIDDEN (status code: 403): Missing Permissions":
                    embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
                    return await bot.say(embed = embed)

        else:
            embed = discord.Embed(description = ":x: You do not have **Valid Permissions**", color = 0x003f80)
            return await bot.say(embed = embed)
###################################

@bot.command(pass_context=True)
async def info(ctx):
    infodesc=("Hello, I'm **Papa** the creator of **Venus** <:discordbotv:394008917916516353>...\n**Venus** is a multi-purpose **Discord bot** made with various commands to help improve your Discord server!") 




    embed = discord.Embed(description="<:venusv:393876481585053707> **~Venus~**", color = 0xcd6800)
    embed.add_field(name="Basic Information",value=infodesc)
    embed.add_field(name="Programming Information",value="**• Version**: Currently in BETA (`v0.0.1`) stage and will be developed furthur! :gear:\n**• Created Using**: Discord.py [async] library :book:\n**• Language**: Python `v3.6.3` <:pythonv:394036103457275905>\n**• Editor**: Visual Studio Code <:VSCv:394043289025773568>")
    embed.set_footer(text="If you require any help use ~ vhelp")
    return await bot.say(embed = embed)
###################################


@bot.command(pass_context = True)
async def help(ctx):
    helpdesc=(":scroll: **Moderator Commands**\n"
              "\n"
              "»» (Bot needs Administrator permissions for these commands)\n"
              "**Prefix = ** `v.`\n"
              "**Important Command:**  `v.setup` \n"
              "\n"
              " • `v.purge <message amount>` → deletes an amount of messages from the channel\n"
              " • `v.getbans` → displays all currently banned members\n"
              " • `v.listservers` → displays all current servers the bot has joined\n"
              " • `v.kick <member mention` → kicks a member\n"
              " • `v.ban <member mention>` → bans a member\n"
              " • `v.unban <member mention>` → unbans a member\n"
              " • `v.warn <member mention> <reason>` → warns a member\n"
              " • `v.mute <member mention> <reason>` → mutes a member\n"
              " • `v.unmute <member mention>` → unmutes a member\n"
              " •`v.createroles` → Creates the bot roles **(ADMIN PERMISSIONS NEEDED)** \n"
              "\n"
              ":scroll: **User Commands**\n"
              "\n"
              "»» (Bot does **NOT** need Administrator permissions for these commands)\n"
              " • `v.ping` → pings the bot\n"
              " • `v.invite` → invites the bot\n"
              " • `v.support` → invite link to the bot's support server \n"
              " • `v.flip` → flips a coin\n")

    


    embed = discord.Embed(description = helpdesc, color = 0xcd6800)
    await bot.send_message(ctx.message.author,embed = embed)
    embed = discord.Embed(description = ":scroll: **|**  I have sent a **Private Message** to you containing my **Command list**", color = 0xcd6800)
    return await bot.say(embed = embed)
    

###################################

@bot.command(pass_context = True)
async def setup(ctx):
    setupdesc=("1. Give the bot **Administrator Permissions**\n"
               "2. Use the `v.createroles` command to create needed roles (`v.help` for information)\n"
               "3. To use **Moderator** commands, give the specified user the **Venus Mod** role\n"
               "*Note:  Ignore the **Venus Muted** role (It will be used for the mute command)*")

    embed = discord.Embed(title="Setup",description = setupdesc, color = 0xcd6800)
    await bot.send_message(ctx.message.author,embed = embed)
    embed = discord.Embed(description = ":scroll: **|**  I have sent a **Private Message** to you containing my **Setup instructions**", color = 0xcd6800)
    return await bot.say(embed = embed)

###############################

''' class BannedMember(commands.Converter):
    async def convert(self, ctx, arg):
        bans = await ctx.guild.bans()

        try:
            member_id = int(arg)
            user = discord.utils.find(lambda u: u.user.id == member_id, bans)
        except ValueError:
            user = discord.utils.find(lambda u: str(u.user) == arg, bans)

        if user is None:
            return None

        return user '''











###################################
######### MEMBER COMMANDS #########
###################################


@bot.command(pass_context = True)
async def flip(ctx):
    flipnumber=random.randint(0,1)
    if flipnumber == 0:
        embed = discord.Embed(description = "**Heads**", color = 0xcd6800)
        return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = "**Tails**", color = 0xcd6800)
        return await bot.say(embed = embed)

###################################

@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(description = "**Invite**: https://discordapp.com/oauth2/authorize/?permissions=2138569983&scope=bot&bot_id=382933981357932545", color = 0xcd6800)
    return await bot.say(embed = embed)

###################################

@bot.command(pass_context=True)
async def support(ctx):
    embed = discord.Embed(description = "**Support Server**: https://discord.gg/puz7474", color = 0xcd6800)
    return await bot.say(embed = embed)

###################################
@bot.command(pass_context=True)
async def ping(ctx, *args):
    t1 = time.perf_counter()
    await bot.send_typing(ctx.message.channel)
    t2 = time.perf_counter()
    embed = discord.Embed(description = ":ping_pong: **Pong!** ```{}ms```".format(round((t2 - t1) * 1000)) , color = 0xcd6800)
    return await bot.say(embed = embed)


###################################
####### Developer COMMANDS ########
###################################

@bot.command(pass_context=True, no_pm=True)
async def shutdown(ctx):
    author = '337309362575900672'
    if author == ctx.message.author.id:
        
            embed = discord.Embed(title="**Shutdown**", description = " **Venus** has been **Shutdown** for Maintenance! :gear:", color = 0x9370db)
            embed.set_footer(text = time.strftime("%d/%m/%Y - %H:%M:%S"))
            await bot.say(embed=embed)
            await bot.logout()
    else:
            embed = discord.Embed(description = "***Developer Command Only!***", color = 0x9370db)
            return await bot.say(embed = embed)

@bot.command(pass_context=True, no_pm=True)
async def reboot(ctx):
    author = '337309362575900672'
    if author == ctx.message.author.id:
        
            embed = discord.Embed(title="**Reboot**", description = " **Venus** Is **Rebooting** for Maintenance! **Please Wait...** :gear:", color = 0x9370db)
            embed.set_footer(text = time.strftime("%d/%m/%Y - %H:%M:%S"))
            await bot.say(embed=embed)
            os.execve(sys.executable, ['python'] + sys.argv, os.environ)
    else:
            embed = discord.Embed(description = "***Developer Command Only!***", color = 0x9370db)
            return await bot.say(embed = embed)


@bot.command(pass_context=True, no_pm=True)
async def username(ctx,*,name : str):
    author = '337309362575900672'
    if author == ctx.message.author.id:
        
            embed = discord.Embed(title="**Username**", description = " **Bot username changed** to: `_"+name+"` :gear:", color = 0x9370db)
            embed.set_footer(text = time.strftime("%d/%m/%Y - %H:%M:%S"))
            await bot.edit_profile(username=name)
            await bot.say(embed=embed)
    else:
            embed = discord.Embed(description = "***Developer Command Only!***", color = 0x9370db)
            return await bot.say(embed = embed)



###################################
####### Moderator COMMANDS ########
###################################

@bot.command(pass_context=True)
async def mute(ctx, member : discord.Member,*, reason=None):
    serverroles=ctx.message.server.roles
    author=ctx.message.author
    if "Venus Mod" in [x.name for x in serverroles]:
        if 'venus mod' in [r.name.lower() for r in author.roles]:
            if member == author:
                embed = discord.Embed(description = ":x: You cannot **Mute** yourself", color = 0x003f80)
                return await bot.say(embed = embed)
            elif not reason:    
                reason="No Reason Specified"
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = False
                await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
                role = discord.utils.get(ctx.message.server.roles, name="Venus Muted")
                author=ctx.message.author
                await bot.add_roles(member, role)
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Mute <:mutev:393881266618892309>" , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.add_field(name="Reason:", value=":small_blue_diamond:  "+reason, inline=False)
                embed.set_footer(text="Time of Mute:"+time.strftime("%d/%m/%Y - %H:%M:%S"))               
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Muted** on `"+ctx.message.server.name+"` for Reason: **"+reason+"**")

            else:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = False
                await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
                role = discord.utils.get(ctx.message.server.roles, name="Venus Muted")
                author=ctx.message.author
                await bot.add_roles(member, role)
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Mute <:mutev:393881266618892309>" , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.add_field(name="Reason:", value=":small_blue_diamond:  "+reason, inline=False)
                embed.set_footer(text="Time of Mute: "+time.strftime("%d/%m/%Y - %H:%M:%S"))    
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Muted** on `"+ctx.message.server.name+"` for Reason: **"+reason+"**")
                    

        else:
            embed = discord.Embed(description = ":x: **Invalid Permissions** ~ **'Venus Mod'** Role Needed", color = 0x003f80)
            return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
        return await bot.say(embed = embed)

###################################

@bot.command(pass_context=True)
async def unmute(ctx,*, member : discord.Member):
    serverroles=ctx.message.server.roles
    if "Venus Mod" in [x.name for x in serverroles]:
        if 'venus mod' in [r.name.lower() for r in ctx.message.author.roles]:
            server=ctx.message.server
            author=ctx.message.author
            if member == author:
                embed = discord.Embed(description = ":x: You cannot **Unmute** yourself", color = 0x003f80)
                return await bot.say(embed = embed)
            else:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = True
                await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)
                role = discord.utils.get(server.roles, name="Venus Muted")
                await bot.remove_roles(member, role)
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Unmute <:unmutev:393881546123378703>" , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.set_footer(text="Time of Unmute:"+time.strftime("%d/%m/%Y - %H:%M:%S"))               
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Unmuted** on `"+ctx.message.server.name+"`")
        else:
            embed = discord.Embed(description = ":x: **Invalid Permissions** ~ **'Venus Mod'** Role Needed", color = 0x003f80)
            return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
        return await bot.say(embed = embed)
    
###################################

@bot.command(pass_context=True)
async def warn (ctx,member : discord.Member = None,*,reason=None):
    serverroles=ctx.message.server.roles
    servermembers=ctx.message.server.roles
    if "Venus Mod" in [x.name for x in serverroles]:
        if 'venus mod' in [r.name.lower() for r in ctx.message.author.roles]:
            author=ctx.message.author
            if member == author:
                embed = discord.Embed(description = ":x: You cannot **Warn** yourself", color = 0x003f80)
                return await bot.say(embed = embed)
            elif not reason:
                reason="No Reason Specified"
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Warn :warning: " , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.add_field(name="Reason:", value=":small_blue_diamond:  "+reason, inline=False)
                embed.set_footer(text="Time of Warn: "+time.strftime("%d/%m/%Y - %H:%M:%S"))    
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Warned** on `"+ctx.message.server.name+"` for Reason: **"+reason+"**")


            else:
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Warn :warning: " , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.add_field(name="Reason:", value=":small_blue_diamond:  "+reason, inline=False)
                embed.set_footer(text="Time of Warn: "+time.strftime("%d/%m/%Y - %H:%M:%S"))    
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Warned** on `"+ctx.message.server.name+"` for Reason: **"+reason+"**")


        else:
            embed = discord.Embed(description = ":x: **Invalid Permissions** ~ **'Venus Mod'** Role Needed", color = 0x003f80)
            return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
        return await bot.say(embed = embed)

###################################

@bot.command(pass_context=True)
async def purge(ctx, number : int):
    serverroles=ctx.message.server.roles
    if "Venus Mod" in [x.name for x in serverroles]:
        if 'venus mod' in [r.name.lower() for r in ctx.message.author.roles]:

            mgs = []
            number = int(number)
            if number ==0 or number < 0:
                embed = discord.Embed(description = ":x: Message amount **Cannot** be **0** or **Less**", color = 0x003f80)
                return await bot.say(embed = embed)           
            else:
                try:
                    purges= await bot.purge_from(ctx.message.channel, limit=int(number) + 1)
                    purged=len(purges)
                    embed = discord.Embed(description = ":white_check_mark: **Purge Successful** | `"+str(purged)+"` Message(s) **Deleted**", color = 0x27004d)
                    return await bot.say(embed = embed)
                except Exception as e:
                    if str(e)=="BAD REQUEST (status code: 400): You can only bulk delete messages that are under 14 days old.":
                        embed = discord.Embed(description = ":x: You can only delete messages under **14 Days** old", color = 0x003f80)
                        return await bot.say(embed = embed)  
                        
        else:
            embed = discord.Embed(description = ":x: **Invalid Permissions** ~ **'Venus Mod'** Role Needed", color = 0x003f80)
            return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
        return await bot.say(embed = embed)

###################################

@bot.command(pass_context = True)
async def getbans(ctx):
    serverroles=ctx.message.server.roles
    if "Venus Mod" in [x.name for x in serverroles]:
        if 'venus mod' in [r.name.lower() for r in ctx.message.author.roles]:
            x = await bot.get_bans(ctx.message.server)
            x = '\n'.join([str(y) for y in x])
            if x =="":
                x="***(None)***"
                embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xcd6800)
                return await bot.say(embed = embed)


            else:
                embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xcd6800)
                return await bot.say(embed = embed)

        else:
            embed = discord.Embed(description = ":x: **Invalid Permissions** ~ **'Venus Mod'** Role Needed", color = 0x003f80)
            return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
        return await bot.say(embed = embed)

###################################

@bot.command(pass_context=True)
async def unban(ctx,*, member):
    serverroles=ctx.message.server.roles
    if "Venus Mod" in [x.name for x in serverroles]:
        if 'venus mod' in [r.name.lower() for r in ctx.message.author.roles]:
            server=ctx.message.server
            bans = await bot.get_bans(server)
            try:
                uid = int(member)
                matches = list(filter(lambda u: u.id == uid, bans))
                if not matches:
                    embed = discord.Embed(description = ":x: No Matches **Found**", color = 0x003f80)
                    return await bot.say(embed = embed)
                _member = matches[0]

            except ValueError:
                matches = list(filter(lambda u: str(u) == member, bans))
                if not matches:
                    embed = discord.Embed(description = ":x: No Matches **Found**", color = 0x003f80)
                    return await bot.say(embed = embed)
                _member = matches[0]
            try:
                await bot.unban(ctx.message.server, _member )
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Unban <:vbanhammer:402120760157536266>" , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.set_footer(text="Time of Unban: "+time.strftime("%d/%m/%Y - %H:%M:%S"))               
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Unbanned** from `"+ctx.message.server.name+"`")
            except:
                return


                

                


           
        else:
                embed = discord.Embed(description = ":x: **Invalid Permissions** ~ **'Venus Mod'** Role Needed", color = 0x003f80)
                return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
        return await bot.say(embed = embed)

###################################

@bot.command(pass_context = True)
async def ban(ctx,member : discord.Member = None,*, reason=None):
    serverroles=ctx.message.server.roles
    if "Venus Mod" in [x.name for x in serverroles]:
        if 'venus mod' in [r.name.lower() for r in ctx.message.author.roles]:
            author=ctx.message.author
            if member == author:
                embed = discord.Embed(description = ":x: You cannot **Ban** yourself", color = 0x003f80)
                return await bot.say(embed = embed)
            elif not reason:
                reason="No Reason Specified"
                await bot.ban(member)
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Ban <:vbanhammer:402120760157536266>" , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.add_field(name="Reason:", value=":small_blue_diamond:  "+reason, inline=False)
                embed.set_footer(text="Time of Ban: "+time.strftime("%d/%m/%Y - %H:%M:%S"))               
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Banned** from `"+ctx.message.server.name+"` for Reason: **"+reason+"**")


            else:
                await bot.ban(member)
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Ban <:vbanhammer:402120760157536266>" , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.add_field(name="Reason:", value=":small_blue_diamond:  "+reason, inline=False)
                embed.set_footer(text="Time of Ban: "+time.strftime("%d/%m/%Y - %H:%M:%S"))               
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Banned** from `"+ctx.message.server.name+"` for Reason: **"+reason+"**")

        else:
            embed = discord.Embed(description = ":x: **Invalid Permissions** ~ **'Venus Mod'** Role Needed", color = 0x003f80)
            return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
        return await bot.say(embed = embed)

###################################

@bot.command(pass_context = True)
async def kick(ctx,member : discord.Member = None,*, reason=None):
    serverroles=ctx.message.server.roles
    if "Venus Mod" in [x.name for x in serverroles]:
        if 'venus mod' in [r.name.lower() for r in ctx.message.author.roles]:
            author=ctx.message.author
            if member == author:
                embed = discord.Embed(description = ":x: You cannot **Kick** yourself", color = 0x003f80)
                return await bot.say(embed = embed)
            elif not reason:
                reason="No Reason Specified"
                await bot.kick(member)
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Kick :boot:" , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.add_field(name="Reason:", value=":small_blue_diamond:  "+reason, inline=False)
                embed.set_footer(text="Time of Kick: "+time.strftime("%d/%m/%Y - %H:%M:%S"))               
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Kicked** from `"+ctx.message.server.name+"` for Reason: **"+reason+"**")




            else:
                await bot.kick(member)
                embed = discord.Embed(color = 0x27004d)
                embed.set_thumbnail(url="https://i.imgur.com/Tg0cMP1.png")
                embed.add_field(name="Action:", value="Kick :boot:" , inline=False)
                embed.add_field(name="User:", value=":small_blue_diamond:  "+member.name, inline=False)
                embed.add_field(name="Author:", value=":small_blue_diamond:  "+ctx.message.author.name, inline=False)
                embed.add_field(name="Reason:", value=":small_blue_diamond:  "+reason, inline=False)
                embed.set_footer(text="Time of Kick:"+time.strftime("%d/%m/%Y - %H:%M:%S"))               
                await bot.say(embed = embed)
                return await bot.send_message(member,":white_check_mark: You have been **Kicked** from `"+ctx.message.server.name+"` for Reason: **"+reason+"**")

        else:
            embed = discord.Embed(description = ":x: **Invalid Permissions** ~ **'Venus Mod'** Role Needed", color = 0x003f80)
            return await bot.say(embed = embed)
    else:
        embed = discord.Embed(description = ":x: **Venus** does not have **Valid Permissions** for this command", color = 0x003f80)
        return await bot.say(embed = embed)

###################################

@bot.command(pass_context = True)
async def listservers(ctx):
    x = '\n'.join([str(server) for server in bot.servers])
    embed = discord.Embed(title = "Servers:", description = x, color = 0xcd6800)
    return await bot.say(embed = embed)

###################################



bot.run('Token')
