let tg = window.Telegram.WebApp;

tg.expand();

// tg.MainButton.textColor = '#fff';
// tg.MainButton.color = '#ff00ff';


const onClose = () => {
	tg.close();
}

let username = document.getElementById('username');
username.innerText = tg.initDataUnsafe?.user?.username;
