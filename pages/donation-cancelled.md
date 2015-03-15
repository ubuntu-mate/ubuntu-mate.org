<!--
.. title: Cancelled Donation
.. slug: donation-cancelled
.. date: 2014-11-04 22:23:23
.. tags: 
.. link: 
.. description:
-->

<style>
img.centered {
    display: block;
    margin-left: auto;
    margin-right: auto }
</style>

<div class="alert alert-error"><strong>Cancelled</strong> You cancelled your donation.</div>

Please reconsider, We've spent a great deal of time creating Ubuntu MATE
and it is nice when the effort is recognised. As a donor, you'll be
helping to cover our hosting costs and reward contributors to the project.

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

<div class="bs-component">
    <div class="jumbotron">
        <h1>Oh well!</h1>
        <p>Strapped for cash? Yeah, we understand. Stop by and donate when you can spare the money.</p>
        <a href="/" class="btn btn-primary btn-lg">Back to the site</a>
        </p>
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
