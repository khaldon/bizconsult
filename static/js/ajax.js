const EmailNewsletterTop= document.querySelector("#form");
const EmailNewsletterFooter = document.querySelector("#footer_form")
const messageTopPreviewer = document.querySelector("#message")
const messageFooterPreviewer  = document.querySelector("#message_footer")
function handleSubmit(postForm, url, method, messagePreview) {
    postForm.addEventListener("submit", e => {
        e.preventDefault();
        formData = new FormData(postForm);
        fetch(url, {
                method: method,
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                document.querySelector('.loader').style.display = 'block';
                postForm.reset();
                let message = data['message']
                messagePreview.innerHTML = message
                if(message == 'Thank you for subscribing'){
                    setTimeout(() => {  messagePreview.style.display = 'none'; }, 2500);
                }else{ messagePreview.style.display = 'block'}
                document.querySelector('.loader').style.display = 'none';

            })
            .catch((error) => {
                console.error('Error:', error);
            });

    })
}
handleSubmit(EmailNewsletterTop, '', 'post', messageTopPreviewer)
handleSubmit(EmailNewsletterFooter, '', 'post', messageFooterPreviewer)

