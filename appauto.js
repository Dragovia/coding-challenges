// Time Left ID's

for (let t = 1; t < 19; t++) {
  document.getElementById("timeLeft" + t)
}
// Birthday People ID's
for (let p = 1; p < 19; p++) {
  document.getElementById("bp" + p)
}

// Birthdays ID's
for (let d = 1; d < 19; d++) {
  document.getElementById("bd" + d)
}
for (let birthday = 1; birthday < 19; birthday++) {
  document.getElementById("birthday" + birthday)
}

for (let x = 1; x < 19; x++) {
  document.getElementById("date" + x)
}

// Time Units
const second = 1000
const minute = second * 60
const hour = minute * 60
const day = hour * 24

// Arrays: Birthdays, Text Dates, and Names

// Removed Birthdays: Lifted Feb 7, Cerise Feb 22, Fellatrix Lestrange Nov 7, Robert71 Nov 8, SonofAnarchy Sep 6, Deadly_Dahlia Nov 7, Whitewolf Nov 23, Cerise Feb 22, MidnightGhost Mar 12

const birthdayArray = ['02/14/2024', '03/24/2024', '03/27/2024', '03/28/2024', '04/12/2024', '05/22/2024', '07/08/2024', '07/17/2024', '08/03/2024', '08/17/2024', '09/03/2024', '09/30/2024', '10/10/2024', '10/15/2024', '11/07/2024', '12/02/2024', '12/10/2024', '12/13/2024', '12/15/2024', '12/26/2024', '12/29/2024']

const nameArray = ['Coffee Dragon', 'Zeus', 'Fierce', 'pagag60', 'Viper99', 'Bad Cherub', 'Willow', 'Jackie', 'Lucifer', 'MR1776', 'Kermit', 'FrenchSarah', 'BeautifulBadass', 'jade30', 'VinneThePooh','Crimson Tide', 'RedMischief', 'Julia', 'Mousey', 'Shy', 'Till']

const nameDateArray = ['Feb 14', 'Mar 24', 'Mar 27', 'Mar 28', 'Apr 12', 'May 22', 'Jul 8', 'Jul 17', 'Aug 3', 'Aug 17', 'Sep 3', 'Sep 30', 'Oct 10', 'Oct 15', 'Nov 7', 'Dec 2', 'Dec 10', 'Dec 13', 'Dec 15', 'Dec 26', 'Dec 29']

// FOR LOOP CONTAINING TOP SPOT

for (let i = 0; i < birthdayArray.length; i++) {
  const today = new Date()
  const checkDate = new Date(birthdayArray[i])
  const isToday = (checkToday) => {
    const today = new Date()
    return checkToday.getDate() === today.getDate() &&
        checkToday.getMonth() === today.getMonth() &&
        checkToday.getFullYear() === today.getFullYear()
  }
  const checkToday = new Date(birthdayArray[i])
  console.log(isToday(checkToday))
  if (isToday(checkToday) === true) {
    console.log('Today\'s birthday is ' + birthdayArray[i])
    topSpot = i
    break
  }
  const timeSpan = checkDate - today
  console.log(timeSpan)
  if (timeSpan > 0) {
    console.log('The last birthday was ' + birthdayArray[i - 1])
    topSpot = i
    break
  } else {
    topSpot = 0
  }
  
}

// FOR LOOP CONTAINING PEOPLE AND DATES

for (let i = 0; i < birthdayArray.length; i++) {
  var pointer = (i + topSpot) % birthdayArray.length
  //console.log(pointer)
  const today = new Date()
  const checkDate = new Date(birthdayArray[i])
  const checkDate2 = new Date(birthdayArray[pointer])
  const timeSpan = checkDate - today
  const timeSpan2 = checkDate2 - today
  var days = Math.floor(timeSpan / day) + 1
  var days2 = Math.floor(timeSpan2 / day) + 1
  person = document.getElementById('bp' + (i + 1))
  birthdate = document.getElementById('bd' + (i + 1))
  birthslot = document.getElementById('birthday' + (i + 1))
  countdown = document.getElementById('timeLeft' + (i + 1))
  // console.log(person)
  // console.log(birthdate)
  person.innerHTML = `${nameArray[pointer]}`
  birthdate.innerHTML = `${nameDateArray[pointer]}`
  

  // var days2 = -1
  if (days2 < 0) {
    days2 = 365 + days2
  }
  countdown.innerHTML = `${days2} days left`
  if (days2 < 8) {
    countdown.innerHTML = `Soon, just ${days2} days left`
    birthslot.classList.add('birthdaysoon')
  }
  if (days2 === 1) {
    countdown.innerHTML = 'Tomorrow\'s the big day!'
    birthslot.classList.add('birthdaysoon')
  }
  if (days2 === 0) {
    countdown.innerHTML = 'Happy Birthday!'
    birthslot.classList.remove('birthdaysoon')
    birthslot.classList.add('itsyourbirthday')
  }
  if (days2 > 360) {
    countdown.innerHTML = 'Hope you had a nice Birthday!'
    birthslot.classList.remove('itsyourbirthday')
    birthslot.classList.add('birthdaypast')
  }
}