---
layout: blog-post
title: Running Steam on Ubuntu MATE
permalink: running-steam-on-ubuntu-mate
description: Ubuntu MATE makes an ideal Steam platform for Linux, find out how to get the optimum experience
category: news
author: Martin Wimpress
lang: en
---

A couple of weeks ago [Phoronix published an article comparing the Steam 
performance on various flavours of Ubuntu 
16.04](http://www.phoronix.com/scan.php?page=article&item=ubuntu-xenial-skldesk). 
This article made me very sad because, using the default settings, Ubuntu MATE didn't 
appear to fair that well. I was also somewhat surprised, what with Ubuntu MATE 
sharing a good deal in common with the other flavours and being a fairly 
light-weight operating system. While I'm not a big gamer, I've always been 
very satisfied with Steam performance on Ubuntu MATE.

What we need here is a gamer. A gaming enthusiast who knows how to run a 
benchmark. A Linux gamer. Enter **[Pedro 
Mateus](https://twitter.com/UnaccountedFour)** from **[Linux Game 
Cast](https://linuxgamecast.com/)**.

<p align="center">
[Steam on Ubuntu MATE](/gallery/blog/steam-on-ubuntu-mate.png)

Pedro ran the benchmarks he is most familar with on his Steam Box by simply 
replacing the SSD with one that had Ubuntu MATE 16.04 installed. Pedro also 
tested all the available compositor options available in Ubuntu MATE, 
afterall, we've included a number of compositor options to suit different use 
cases. This is the hardware, software and configuration used:

<div class="row" name="system_spec">
  <div class="col-xs-4">
    <div class="bs-component">
      <div class="list-group">
        <a class="list-group-item active">Hardware</a>
        <a class="list-group-item">AMD Athlon X4 860K @ 4.2Ghz</a>
        <a class="list-group-item">MSI GeForce GTX 750Ti OC Edition</a>
        <a class="list-group-item">8GB DDR3 1866MHz HyperX White</a>
        <a class="list-group-item">OCZ Vertex 3 120GB SSD</a>
      </div>
    </div>
  </div>
  <div class="col-xs-4">
    <div class="bs-component">
      <div class="list-group">
        <a class="list-group-item active">Software</a>
        <a class="list-group-item">Ubuntu MATE 16.04 64-bit</a>
        <a class="list-group-item">Nvidia proprietary drivers 364.15</a>
        <a class="list-group-item">Multi-Sample AA – Off</a>
        <a class="list-group-item">&nbsp;</a>        
      </div>    
    </div>
  </div>
  <div class="col-xs-4">
    <div class="bs-component">
      <div class="list-group">
        <a class="list-group-item active">Talos Principle</a>
        <a class="list-group-item">CPU Speed - Ultra</a>
        <a class="list-group-item">GPU Speed - Medium</a>
        <a class="list-group-item">GPU Memory - High</a>
        <a class="list-group-item">Level Caching - Medium</a>
      </div>    
    </div>
  </div>  
</div>

All benchmarks were run at 1920x1080. The table below shows the **average
frames per second** for each benchmark. The colouring of the average
frames per second denotes how much, if any, screen tearing was visible.

  * <span class="btn btn-danger btn-xs">Bad tearing</span>

  * <span class="btn btn-warning btn-xs">Noticeable tearing</span>

  * <span class="btn btn-success btn-xs">No noticeable tearing</span>

<table class="table table-striped table-hover">
  <thead>
    <tr>
      <th>Benchmark</th>
      <th>No compositor</th>
      <th>Software compositor</th>
      <th>Compton</th>
      <th>Compiz</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://unigine.com/products/benchmarks/heaven/">Unigine Heaven</a> – <b>Extreme</b></td>
      <td><span class="btn btn-danger btn-xs">25.5</span></td>
      <td><span class="btn btn-warning btn-xs">25.1</span></td>
      <td><span class="btn btn-success btn-xs">25.0</span></td>
      <td><span class="btn btn-success btn-xs">24.9</span></td>
    </tr>
    <tr>
      <td><a href="https://unigine.com/products/benchmarks/heaven/">Unigine Heaven</a> – <b>Basic</b></td>    
      <td><span class="btn btn-success btn-xs">88.1</span></td>
      <td><span class="btn btn-success btn-xs">84.6</span></td>
      <td><span class="btn btn-success btn-xs">84.4</span></td>
      <td><span class="btn btn-success btn-xs">84.0</span></td>
    </tr>
    <tr>
      <td><a href="http://store.steampowered.com/app/257510/">The Talos Principle</a> – <b>OpenGL</b></td>    
      <td><span class="btn btn-warning btn-xs">70.4</span></td>
      <td><span class="btn btn-warning btn-xs">68.5</span></td>
      <td><span class="btn btn-success btn-xs">70.3</span></td>
      <td><span class="btn btn-success btn-xs">69.8</span></td>            
    </tr>
    <tr>
      <td><a href="http://store.steampowered.com/app/257510/">The Talos Principle</a> – <b>Vulkan</b></td>    
      <td><span class="btn btn-success btn-xs">97.1</span></td>
      <td><span class="btn btn-success btn-xs">89.9</span></td>
      <td><span class="btn btn-success btn-xs">96.9</span></td>
      <td><span class="btn btn-success btn-xs">95.1</span></td>
    </tr>
  </tbody>
</table>
<br />

## Conclusions

So what do we learn from the benchmarks above?

  * The Ubuntu MATE default Window Manager is *Marco (Software compositor)*.
  This **explains why the Phoronix benchmarks didn't show Ubuntu MATE in
  the best light**, since it can be the lowest performing option for gaming.
    * Perhaps Marco needs some logic to Unredirect Fullscreen Windows.
  * Using **Compton or Compiz provides tear free gaming**.
  * **Compton (slightly) out performs Compiz**.
  * Perdro tells me that when **running Ubuntu MATE with Compton the average
  frames per second is about 2 FPS lower than SteamOS** on the same
  hardware.
    * This seems reasonable given that Ubuntu MATE is a general purpose
    desktop operating system and SteamOS is purpose built for gaming.
  * **Vulkan is [the cat's pyjamas](http://www.urbandictionary.com/define.php?term=Cats%20pajamas)!**

From the benchmarks [Pedro Mateus](https://plus.google.com/+PedroMateus) 
conducted **we can recommend that to get the optimum gaming experience on 
Ubuntu MATE you should use Compton**, which can be enable via MATE Tweak, and 
that **Ubuntu MATE gaming performance is just about on par with SteamOS**.
