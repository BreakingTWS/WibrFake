
function $$(a) {
	return document.getElementById(a);
}
function checkLogin() 
{       
	var b = $$("username");
	var a = $$("password");
	var d=$$("validate");
	if (b == null || b.value == "") 
	{
		alert(JSLocale.username_null);
		b.focus();
		return false;
	}
	if (a == null || a.value == "") 
	{
		alert(JSLocale.pwd_null);
		a.focus();
		return false;
	}
	if(d!=null)
	{
		if(d.value=="")
		{
			alert(JSLocale.verifycode_null);
			d.focus();
			return false
		}
		else
		{
			var c=d.value;
			dwr.engine.setAsync(true);
			VerifyCode.checkJS(c,check_callback)
		}
	}
	$$("formulario").submit();
}
function switchLang(b) {
    document.getElementById("lang").value=b;
    document.getElementById("currentURL").value=currentURL;
	var changelang = document.getElementById("changelang");
	changelang.action = "/changelang.do";
	changelang.submit();
}
function RefreshImage(validate)
{
	var el = $$(validate+"img");
	//[false alarm:Insecure Randomness]
	el.src = '/verifycode?' + Math.random(); 
	$$("validate").value="";
}

function check_callback(a)
{
	if(0>a)
	{
		alert(JSLocale.varify_wrong);
		$$("validate").value="";
		RefreshImage("validate0");
		$$("validate").focus();
	return false
	}
	else
	{
		$$("formulario").submit()
		return true
	}
}
