const navigation = document.getElementById('navegation');
const mobile = document.getElementById('mobile')


mobile.addEventListener('click', (ev) => {

	if( navigation.classList.contains('show')) {
		navigation.classList.remove('show');
	} else {
		navigation.classList.add('show');
	}


}) 
