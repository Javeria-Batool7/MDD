async function signup(e) {
  e.preventDefault();
  const email = document.getElementById("email");
  const name = document.getElementById("username");
  const passs = document.getElementById("password");
  console.log(email.value, passs.value)
  try {
    const result = await firebase.auth().createUserWithEmailAndPassword(email.value, passs.value);
    const uid = firebase.auth().currentUser.uid;
    const dic = { "name": name.value, "email": email.value }
    firebase.database().ref(`user/${uid}`).set(dic);
    M.toast({ html: "Succesfully Signed Up, Lets Sign In!!", classes: 'green' });
    jQuery_3_6_1("main").removeClass("sign-up-mode");
    email.value = "";
    passs.value = "";
    name.value = "";
    
  }
  catch (e) {
    console.log(e);
    M.toast({ html: e.message, classes: 'red' });
    email.value = "";
    passs.value = "";
    name.value = "";
  }

}

async function signin(e) {
  e.preventDefault();
  const email = document.getElementById("username_");
  const passs = document.getElementById("password_");
  console.log(email.value, passs.value)
  try {
    const result = await firebase.auth().signInWithEmailAndPassword(email.value, passs.value);
    M.toast({ html: ` Welcome ${email.value}`, classes: 'green' });
    var delayInMilliseconds = 1000; //1 second
console.log(result);
    setTimeout(function () {
      localStorage.setItem("user_id",firebase.auth().currentUser.uid);
      window.location.href = 'main_page.html';

    }, delayInMilliseconds);

  }
  catch (e) {
    M.toast({ html: e.message, classes: 'red' });
    email.value = "";
    passs.value = "";
  }

}


function logout() {
  var delayInMilliseconds = 1000; //1 second
  localStorage.removeItem("user_id");
  firebase.auth().signOut();
  setTimeout(function () {
    window.location.href = 'index.html';

  }, delayInMilliseconds);

}

// firebase.auth().onAuthStateChanged((user) => {
//   if (user) {
//     console.log(user)

//   } else {
//     console.log("logged Out")
//   }
// });


function Uploadimg() {
  imgs = document.getElementById("imgs");
  aaa = imgs.value.split('\\')
  var currentdate = new Date(); 
var datetime =currentdate.getDate() + "-"+ (currentdate.getMonth()+1)  + "-"  + currentdate.getFullYear() + " @ "  + currentdate.getHours() + ":"   + currentdate.getMinutes() + ":" + currentdate.getSeconds();
if (localStorage.getItem("dateandtime")==null)  {
  // localStorage.setItem("dateandtime",datetime);

  const fileRef = firebase.storage().ref().child(`/users/${localStorage.getItem("user_id")}/${datetime}/${aaa[aaa.length -1]}`);
  var uploadTask = fileRef.put(imgs.files[0]);

  uploadTask.on('state_changed',
    (snapshot) => {
      var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
      if (progress == "100") {
        alert("done")
      }
    },
    (error) => {
      console.log(error)
    },
    () => {

      uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
        // console.log('File available at', downloadURL);
      });
    }
  );
}
else{
  const fileRef = firebase.storage().ref().child(`/users/${localStorage.getItem("user_id")}/${localStorage.getItem("dateandtime")}/${aaa[aaa.length -1]}`);
  var uploadTask = fileRef.put(imgs.files[0]);

  uploadTask.on('state_changed',
    (snapshot) => {
      var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
      if (progress == "100") {
        alert("done")
      }
    },
    (error) => {
      console.log(error)
    },
    () => {

      uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
        // console.log('File available at', downloadURL);
      });
    }
  );
}
  
}

function Uploadmore(){
  
  jQuery_3_6_1("#imgs").val("");
  imgs = document.getElementById("imgs");
  aaa = imgs.value.split('\\')
  var currentdate = new Date(); 
var datetime =currentdate.getDate() + "-"+ (currentdate.getMonth()+1)  + "-"  + currentdate.getFullYear() + " @ "  + currentdate.getHours() + ":"   + currentdate.getMinutes() + ":" + currentdate.getSeconds();
if (localStorage.getItem("dateandtime")==null)  {
  // localStorage.setItem("dateandtime",datetime);

  const fileRef = firebase.storage().ref().child(`/users/${localStorage.getItem("user_id")}/${datetime}/${aaa[aaa.length -1]}`);
  var uploadTask = fileRef.put(imgs.files[0]);

  uploadTask.on('state_changed',
    (snapshot) => {
      var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
      if (progress == "100") {
        alert("done")
      }
    },
    (error) => {
      console.log(error)
    },
    () => {

      uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
        // console.log('File available at', downloadURL);
      });
    }
  );
}
else{
  const fileRef = firebase.storage().ref().child(`/users/${localStorage.getItem("user_id")}/${localStorage.getItem("dateandtime")}/${aaa[aaa.length -1]}`);
  var uploadTask = fileRef.put(imgs.files[0]);

  uploadTask.on('state_changed',
    (snapshot) => {
      var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
      if (progress == "100") {
        alert("done")
      }
    },
    (error) => {
      console.log(error)
    },
    () => {

      uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
        // console.log('File available at', downloadURL);
      });
    }
  );
}

}