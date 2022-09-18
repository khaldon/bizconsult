// AJAX for HomePage 
const EmailNewsletterTop= document.querySelector("#form");
const EmailNewsletterFooter = document.querySelector("#footer_form")

const messageTopPreviewer = document.querySelector("#message")
const messageFooterPreviewer  = document.querySelector("#message_footer")

function handleSubmitHomePage(postForm, url, method, messagePreview) {
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]')
    postForm.addEventListener("submit", e => {
        e.preventDefault();
    formData = new FormData(postForm);

    fetch(url, {
            headers:{
                'X-requested-With':'XMLHttpRequest',
                'Content-Type':'application/json',
                'X-CSRFToken':csrf
            },
            method: method,
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            // document.querySelector('.loader').style.display = 'block';
            postForm.reset();
            let message = data['message']
            messagePreview.innerHTML = message
            if(message == 'Thank you for subscribing'){
                // setTimeout(() => {  messagePreview.style.display = 'none'; }, 2500);
            }else{ messagePreview.style.display = 'block'}

        })
        .catch((error) => {
            console.error('Error:', error);
        });
    })

} 
// check all the elements forms if not None excute the code below 
// if (EmailNewsletterTop){
//     handleSubmitHomePage(EmailNewsletterTop, '', 'post', messageTopPreviewer)
// }
urlCurrentPage  = window.location.href;
if (EmailNewsletterFooter){
    handleSubmitHomePage(EmailNewsletterFooter, '' , 'post', messageFooterPreviewer)
}

// AJAX for contact page 
const contactForm  = document.querySelector("#contact_form")
let contactMessage = document.querySelector("#contact_message")

function handleSubmitContactPage(postForm, url, method){
    postForm.addEventListener("submit", e=>{
        e.preventDefault();
        formData = new FormData(postForm);
        fetch(url, {
            method:method,
            body:formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data['valid'] == 'Thank you for contacting us'){
                contactMessage.innerHTML = data['valid']
                // setTimeout(() => {  contactMessage.style.display = 'none'; }, 2500);
                contactMessage.style.fontsize = '20';
                contactMessage.style.color = 'green';



            }else{
                contactMessage.innerHTML = data['invalid']['email']['0']
                contactMessage.style.fontsize = '20';
                contactMessage.style.color = 'red';
            }
          
        })
        .catch((error) => {
            console.log('Error', error);
        });
    })
}
if (contactForm){
    handleSubmitContactPage(contactForm, '', 'post')
}

// AJAX for quote page 
const quoteForm = document.querySelector("#quote_form")
let quoteMessage = document.querySelector("#quote_message")
function handleSubmitQoutePage(postForm, url, method, quoteMessage){
    postForm.addEventListener("submit", e=>{
    e.preventDefault();
    formData = new FormData(postForm);
    fetch(url, {
        method:method,
        body:formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data['valid'] == 'Thank you for submitting'){
           
            quoteMessage.innerHTML = data['valid']
            // setTimeout(() => {  quoteMessage.style.display = 'none'; }, 2500);
            quoteMessage.style.fontsize = '20';
            quoteMessage.style.color = 'green';
        }else{
            console.log(data['invalid']['email']['0'])
            quoteMessage.innerHTML = data['invalid']['email']['0']
            quoteMessage.style.fontsize = '20';
            quoteMessage.style.color = 'red';
        }
    })
    .catch((error) => {
        console.log('Error', error);
    });
})
}
if (quoteForm){
    handleSubmitQoutePage(quoteForm, '', 'post', quoteMessage)
}
