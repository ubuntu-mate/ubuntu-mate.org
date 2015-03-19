<!-- 
.. title: Donate
.. slug: donate
.. date: 2014-11-05 23:01:09 UTC
.. tags: Ubuntu,MATE,donate
.. link: 
.. description: 
.. type: text
.. author: Martin Wimpress
-->

<style>
img.centered {
    display: block;
    margin-left: auto;
    margin-right: auto }
</style>

The [Ubuntu MATE community has requested a forum that is not hosted via a
social network](https://ubuntu-mate.org/blog/alternative-community-forum-poll/).

The Ubuntu MATE team have decided to use [Discourse](http://www.discourse.org/)
to provide a community space that is not reliant on social networks but this
will require a new, fairly beefy, virtual private server and some additional
subscription services for email notifications. We are asking the Ubuntu MATE
community members to make a small recurring contribution so that we can
provide what you've asked for.

If this funding campaign generates more monthly income than required for our
hosting alone then we will use the surplus to reward contributors, such as
digital artists/designers, provide development bounties for implementing
new features or fixing bugs and to help subsidise the travel expenses of team
members to represent [MATE Desktop](http://mate-desktop.org) and Ubuntu MATE
at FLOSS conferences. If we have sufficient surplus funds we will also donate
to other Open Source projects that Ubuntu MATE depends upon and should we find
ourselves in that fortunate position we will use our new shiny Discourse
community to vote for the worthy beneficiaries.

We have set up a number of payment options that should hopefully suit everyone.
Go on, be brilliant, help grow our community.

## Patreon

This is a unique way to fund an Open Source community and may also potentially
fund or reward contributors for some aspects of Ubuntu MATE development. A
regular monthly income for the Ubuntu MATE project will allow us to better plan
how best to reward our contributors.

<div class="bs-component">
    <div class="jumbotron">
        <h1>Monthly supporter</h1>
        <p>Become a monthly supporter at <a href="http://www.patreon.com/ubuntu_mate">Patreon</a>
        and help grow the Ubuntu MATE community.</p>
        <a href="http://www.patreon.com/ubuntu_mate" class="btn btn-primary btn-lg">Become a Patron</a>
        </p>
    </div>
</div>

## PayPal

<img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal Logo">

We'd prefer you set-up a recurring payment to help ensure the monthly
hosting costs are always covered and they allow us to better plan how to
reward our contributors. That said, one time donations are also
gratefully accepted.

<div class="bs-docs-section">
  <div class="row">
    <div class="col-lg-6">
      <div class="well bs-component">
        <form name="monthly" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateMonthlyForm()" method="post">
          <fieldset>
            <legend>Monthly PayPal supporter</legend>
            <div class="form-group">
              <label for="donationAmount" class="col-lg-4 control-label">Select an amount</label>
              <div class="col-lg-6">
                <input type="radio" name="amt" value="2.50">2.50
                <input type="radio" name="amt" value="5" checked="">5
                <input type="radio" name="amt" value="10">10
              </div>
            </div>          
            <div class="form-group">
              <label for="specifyAmount" class="col-lg-4 control-label">Specify your own amount</label>
              <div class="col-lg-6">      
                <input type="text" name="other" value="" size="5" maxlength="5">              
              </div>
            </div>
            <div class="form-group">
              <label for="select" class="col-lg-4 control-label">Currency</label>
              <div class="col-lg-6">
                <select class="form-control" name="currency_code">
                  <option>EUR</option>
                  <option>USD</option>
                  <option selected="">GBP</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-6">
                <button type="submit" class="btn btn-primary">Monthly Donation</button>
              </div>
            </div>
          </fieldset>
          <input type="hidden" name="cmd" value="_xclick-subscriptions">
          <input type="hidden" name="business" value="6282B4CZGVCB6">
          <input type="hidden" name="item_name" value="Ubuntu MATE Monthly Supporter">
          <input type="hidden" name="no_shipping" value="1">
          <input type="hidden" name="no_note" value="1">
          <input type="hidden" name="charset" value="UTF-8">
          <input type="hidden" name="a3" value="">
          <input type="hidden" name="p3" value="1">
          <input type="hidden" name="t3" value="M">
          <input type="hidden" name="src" value="1">
          <input type="hidden" name="sra" value="1">
          <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">
          <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
        </form>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="well bs-component">
        <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateSingleForm()" method="post">
          <fieldset>
            <legend>One time PayPal donation</legend>
            <div class="form-group">
              <label for="donationAmount" class="col-lg-4 control-label">Select an amount</label>
              <div class="col-lg-6">
                <input type="radio" name="amt" value="2.50">2.50
                <input type="radio" name="amt" value="5" checked="">5
                <input type="radio" name="amt" value="10">10
              </div>
            </div>
            <div class="form-group">
              <label for="specifyAmount" class="col-lg-4 control-label">Specify your own amount</label>
              <div class="col-lg-6">      
                <input type="text" name="other" value="" size="5" maxlength="5">              
              </div>
            </div>
            <div class="form-group">
              <label for="select" class="col-lg-4 control-label">Currency</label>
              <div class="col-lg-6">
                <select class="form-control" name="currency_code">
                  <option>EUR</option>
                  <option>USD</option>
                  <option selected="">GBP</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-6">
                <button type="submit" class="btn btn-primary">Single Donation</button>
              </div>
            </div>
          </fieldset>
          <input type="hidden" name="cmd" value="_xclick">
          <input type="hidden" name="business" value="6282B4CZGVCB6">
          <input type="hidden" name="item_name" value="Ubuntu MATE One-time Donation">
          <input type="hidden" name="no_shipping" value="1">
          <input type="hidden" name="no_note" value="1">
          <input type="hidden" name="charset" value="UTF-8">
          <input type="hidden" name="amount" value="">
          <input type="hidden" name="src" value="1">
          <input type="hidden" name="sra" value="1">
          <input type="hidden" name="return" value="https://ubuntu-mate.org/donation-completed/">
          <input type="hidden" name="cancel_return" value="https://ubuntu-mate.org/donation-cancelled/">
        </form>  
      </div>
    </div>
  </div>
</div>

## Bitcoin and micro payments

<div class="bs-docs-section">
  <div class="row">
    <div class="col-lg-6">
      <div class="well bs-component">
        <legend>Bitcoin</legend>
          <p>Click or scan to QR code below to launch your Bitcoin client and
          donate 0.02 btc to Ubuntu MATE. Alternatively, copy and paste the
          Bitcoin address into your Bitcoin client to donate an amount of your
          choice.</p>
          <p align="center">
            <a href="bitcoin:1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB?amount=0.02&label=Ubuntu%20MATE">
            <img src="https://chart.googleapis.com/chart?chs=192x192&cht=qr&chl=bitcoin:1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB?amount=0.02&message=Donate_0.02_btc_to_Ubuntu_MATE" /></a>
            <br />
            <tt>1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB</tt>
          </p>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="well bs-component">
        <legend>Flattr</legend>
          <p>Maybe you prefer to use a micro payment service? With
          <a href="https://flattr.com/howflattrworks" target="_blank">Flattr</a>,
          supporting creators becomes a natural part of life. Paying for content
          does not only feel good, it makes the world a better place.</p>
          <p align="center">
            <script id='fbjjn1d'>(function(i){var f,s=document.getElementById(i);f=document.createElement('iframe');f.src='//api.flattr.com/button/view/?uid=ubuntumatedotorg&url='+encodeURIComponent(document.URL);f.title='Flattr';f.height=62;f.width=55;f.style.borderWidth=0;s.parentNode.insertBefore(f,s);})('fbjjn1d');</script>
          </p>
      </div>      
    </div>
  </div>
</div>

# Commercial sponsorship

If you are using, or plan to use, Ubuntu MATE in a commercial environment
and would like to sponsor the project more formally then please get in
touch to discuss your requirements.

<div class="bs-docs-section">
  <div class="row">
    <div class="col-lg-12">
      <div class="well bs-component">
        <form class="form-horizontal" action="//forms.brace.io/commercial@ubuntu-mate.org" method="post">
          <fieldset>
            <legend>Send an email</legend>
            <div class="form-group">
              <label for="inputName" class="col-lg-2 control-label">Your name</label>
              <div class="col-lg-10">
                <input autocomplete="off" style="background-image: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAASCAYAAABSO15qAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QsPDhss3LcOZQAAAU5JREFUOMvdkzFLA0EQhd/bO7iIYmklaCUopLAQA6KNaawt9BeIgnUwLHPJRchfEBR7CyGWgiDY2SlIQBT/gDaCoGDudiy8SLwkBiwz1c7y+GZ25i0wnFEqlSZFZKGdi8iiiOR7aU32QkR2c7ncPcljAARAkgckb8IwrGf1fg/oJ8lRAHkR2VDVmOQ8AKjqY1bMHgCGYXhFchnAg6omJGcBXEZRtNoXYK2dMsaMt1qtD9/3p40x5yS9tHICYF1Vn0mOxXH8Uq/Xb389wff9PQDbQRB0t/QNOiPZ1h4B2MoO0fxnYz8dOOcOVbWhqq8kJzzPa3RAXZIkawCenHMjJN/+GiIqlcoFgKKq3pEMAMwAuCa5VK1W3SAfbAIopum+cy5KzwXn3M5AI6XVYlVt1mq1U8/zTlS1CeC9j2+6o1wuz1lrVzpWXLDWTg3pz/0CQnd2Jos49xUAAAAASUVORK5CYII=&quot;); background-repeat: no-repeat; background-attachment: scroll; background-position: right center;" class="form-control" id="inputName" placeholder="Your name" type="text" name="Name">
              </div>
            </div>
            <div class="form-group">
              <label for="inputEmail" class="col-lg-2 control-label">Your email</label>
              <div class="col-lg-10">
                <input autocomplete="off" style="background-image: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAASCAYAAABSO15qAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QsPDhss3LcOZQAAAU5JREFUOMvdkzFLA0EQhd/bO7iIYmklaCUopLAQA6KNaawt9BeIgnUwLHPJRchfEBR7CyGWgiDY2SlIQBT/gDaCoGDudiy8SLwkBiwz1c7y+GZ25i0wnFEqlSZFZKGdi8iiiOR7aU32QkR2c7ncPcljAARAkgckb8IwrGf1fg/oJ8lRAHkR2VDVmOQ8AKjqY1bMHgCGYXhFchnAg6omJGcBXEZRtNoXYK2dMsaMt1qtD9/3p40x5yS9tHICYF1Vn0mOxXH8Uq/Xb389wff9PQDbQRB0t/QNOiPZ1h4B2MoO0fxnYz8dOOcOVbWhqq8kJzzPa3RAXZIkawCenHMjJN/+GiIqlcoFgKKq3pEMAMwAuCa5VK1W3SAfbAIopum+cy5KzwXn3M5AI6XVYlVt1mq1U8/zTlS1CeC9j2+6o1wuz1lrVzpWXLDWTg3pz/0CQnd2Jos49xUAAAAASUVORK5CYII=&quot;); background-repeat: no-repeat; background-attachment: scroll; background-position: right center;" class="form-control" id="inputEmail" placeholder="Email" type="text" name="_replyto">
              </div>
            </div>
            <div class="form-group">
              <label for="inputSubject" class="col-lg-2 control-label">Subject</label>
              <div class="col-lg-10">
                <input autocomplete="off" style="background-image: url(&quot;data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAASCAYAAABSO15qAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QsPDhss3LcOZQAAAU5JREFUOMvdkzFLA0EQhd/bO7iIYmklaCUopLAQA6KNaawt9BeIgnUwLHPJRchfEBR7CyGWgiDY2SlIQBT/gDaCoGDudiy8SLwkBiwz1c7y+GZ25i0wnFEqlSZFZKGdi8iiiOR7aU32QkR2c7ncPcljAARAkgckb8IwrGf1fg/oJ8lRAHkR2VDVmOQ8AKjqY1bMHgCGYXhFchnAg6omJGcBXEZRtNoXYK2dMsaMt1qtD9/3p40x5yS9tHICYF1Vn0mOxXH8Uq/Xb389wff9PQDbQRB0t/QNOiPZ1h4B2MoO0fxnYz8dOOcOVbWhqq8kJzzPa3RAXZIkawCenHMjJN/+GiIqlcoFgKKq3pEMAMwAuCa5VK1W3SAfbAIopum+cy5KzwXn3M5AI6XVYlVt1mq1U8/zTlS1CeC9j2+6o1wuz1lrVzpWXLDWTg3pz/0CQnd2Jos49xUAAAAASUVORK5CYII=&quot;); background-repeat: no-repeat; background-attachment: scroll; background-position: right center;" class="form-control" id="inputSubject" placeholder="Subject" type="text" name="_subject">
              </div>
            </div>
            <div class="form-group">
              <label for="textArea" class="col-lg-2 control-label">Message</label>
              <div class="col-lg-10">
                <textarea class="form-control" rows="3" id="textArea" name="message"></textarea>
                <span class="help-block">Enter you message above and it will be emailed to the Ubuntu MATE commercial team.</span>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-10 col-lg-offset-2">            
                <button type="submit" class="btn btn-primary">Send</button>
              </div>
            </div>
          </fieldset>
          <input type="hidden" name="_next" value="//ubuntu-mate.org/message-sent/" />
          <input type="text" name="_gotcha" style="display:none">
        </form>
      </div>
    </div>
  </div>
</div>

<script type="text/javascript">
  function validateMonthlyForm() {
    var n = document.forms["monthly"]["other"].value;
      if (n) {
        if (!isNaN(parseFloat(n)) && isFinite(n) && (n > 0)) {
          document.forms["monthly"]["a3"].value = n;
          return true;
        } else {
          alert("Please enter a valid donation amount - thanks!");
          document.forms["monthly"]["other"].value = "";
          return false;
        }
      }
      else {
        document.forms["monthly"]["a3"].value = document.forms["monthly"]["amt"].value;
        return true;
      }
  }

  function validateSingleForm() {
    var n = document.forms["single"]["other"].value;
      if (n) {
        if (!isNaN(parseFloat(n)) && isFinite(n) && (n > 0)) {
          document.forms["single"]["amount"].value = n;
          return true;
        } else {
          alert("Please enter a valid donation amount - thanks!");
          document.forms["single"]["other"].value = "";
          return false;
        }
      }
      else {
        document.forms["single"]["amount"].value = document.forms["single"]["amt"].value;
        return true;
      }
  }  
</script>
