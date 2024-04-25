fun tea_request (feat, date_time=250420241630, approval=true) {
  // "approval" is a User Input field & default value is true :p:p
  // "date_time" is also a User Input field & default value is 250420241630

  if(approval){
    if(date_time == 250420241630) return "It works for `{$feat}`"
    else if(date_time > 250420241600 & date_time < 250420241800) return "I will tell you different time for `{$feat}`"
    else return "Really sorry"
  }

  return "Really sorry"

}


in_it = tea_request("ginger tea with less sugar")
