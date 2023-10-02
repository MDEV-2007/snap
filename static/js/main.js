const allStories = [
    {
        thumbUrl: "https://blog.hootsuite.com/wp-content/uploads/2021/02/instagram-shopping-06.png",
        imageUrl: "https://blog.hootsuite.com/wp-content/uploads/2021/02/instagram-shopping-06.png",
        title: "Title No 1"
    },
    {
        thumbUrl: "https://s3.us-west-2.amazonaws.com/images.unsplash.com/small/photo-1584839401450-accbe1a8ef7b",
        imageUrl: "https://s3.us-west-2.amazonaws.com/images.unsplash.com/small/photo-1584839401450-accbe1a8ef7b",
        title: "Title No 2"
    },
    {
        thumbUrl: "https://lh6.googleusercontent.com/KABoo5KazC5V-XnhExwcPUS70rQALPHflJovhvvXJ8FOZ8ecG3LKlq7Mnd8wZB3-7wrSWFcBUNsUOta4Y22XGxkYbkI25Mu8ZqF8eihzzp3GjzML1KaclWHfmw4_5l-t32FXyo-O",
        imageUrl: "https://lh6.googleusercontent.com/KABoo5KazC5V-XnhExwcPUS70rQALPHflJovhvvXJ8FOZ8ecG3LKlq7Mnd8wZB3-7wrSWFcBUNsUOta4Y22XGxkYbkI25Mu8ZqF8eihzzp3GjzML1KaclWHfmw4_5l-t32FXyo-O",
        title: "Title No 3"
    },
    {
        thumbUrl: "https://images.ctfassets.net/az3stxsro5h5/1PbgmPxMCFsZYQTEIMTLIn/ceacc72b9c982b593bc659c66c0658f9/https___later.com_blog_wp-content_uploads_2019_08_Copy-of-TEMPLATE-Vertical-Single-1.png?w=281&h=500&q=50&fm=png",
        imageUrl: "https://images.ctfassets.net/az3stxsro5h5/1PbgmPxMCFsZYQTEIMTLIn/ceacc72b9c982b593bc659c66c0658f9/https___later.com_blog_wp-content_uploads_2019_08_Copy-of-TEMPLATE-Vertical-Single-1.png?w=281&h=500&q=50&fm=png",
        title: "Title No 4"
    },
    {
        thumbUrl: "https://www.socialpilot.co/wp-content/uploads/2021/08/story-saver-app.jpg",
        imageUrl: "https://www.socialpilot.co/wp-content/uploads/2021/08/story-saver-app.jpg",
        title: "Title No 5"
    },
    {
        thumbUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGkCd6xzzCwk9N4dWWDPM3ohPkok4MakQP0w&usqp=CAU",
        imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGkCd6xzzCwk9N4dWWDPM3ohPkok4MakQP0w&usqp=CAU",
        title: "Title No 6"
    },
    {
        thumbUrl: "https://www.socialpilot.co/wp-content/uploads/2021/08/story-saver-app.jpg",
        imageUrl: "https://www.socialpilot.co/wp-content/uploads/2021/08/story-saver-app.jpg",
        title: "Title No 5"
    },
    {
        thumbUrl: "https://www.socialpilot.co/wp-content/uploads/2021/08/story-saver-app.jpg",
        imageUrl: "https://www.socialpilot.co/wp-content/uploads/2021/08/story-saver-app.jpg",
        title: "Title No 5"
    },
    {
        thumbUrl: "https://www.socialpilot.co/wp-content/uploads/2021/08/story-saver-app.jpg",
        imageUrl: "https://www.socialpilot.co/wp-content/uploads/2021/08/story-saver-app.jpg",
        title: "Title No 5"
    },
   
]

const storiesContainer = document.querySelector(".storis-container");
const storyFull = document.querySelector(".story-full");
const storyFullImage = document.querySelector(".story-full img");
const storyFullTitle = document.querySelector(".story-full .title");
const closeBtn = document.querySelector(".story-full .close-btn");
const leftArrow = document.querySelector(".story-full .left-arrow");
const rightArrow = document.querySelector(".story-full .right-arrow");

let currentIndex = 0;

let timer;


allStories.forEach((s, i) =>{
    const content = document.createElement("div");
    content.classList.add("content");

    const img = document.createElement("img");
    img.setAttribute("src", s.thumbUrl)

    storiesContainer.appendChild(content) ;
    content.appendChild(img);

    content.addEventListener("click", () => {
        currentIndex = i;
        storyFull.classList.add('active');
        storyFullImage.setAttribute('src', s.imageUrl);

        if (!s.title) {
            storyFullTitle.style.display = 'none';
        }else{
            storyFullTitle.style.display = 'block';
            storyFullTitle.innerHTML = s.title
        }
        clearInterval(timer);
        timer = setInterval(nextStory, 5000)
    })

})

closeBtn.addEventListener("click", () => {
    storyFull.classList.remove('active');
})

leftArrow.addEventListener("click", () => {
    if (currentIndex > 0) {
        currentIndex -= 1;
       
        storyFullImage.setAttribute('src', allStories[currentIndex].imageUrl);

        if (!allStories[currentIndex].title) {
            storyFullTitle.style.display = 'none';
        } else { 
            storyFullTitle.style.display = 'block';
            storyFullTitle.innerHTML = allStories[currentIndex].title;
        }

        clearInterval(timer);
        timer = setInterval(nextStory, 5000)
    }
});


rightArrow.addEventListener("click", () => {
    if (currentIndex < allStories.length - 1) {
        currentIndex += 1;
       
        storyFullImage.setAttribute('src', allStories[currentIndex].imageUrl);

        if (!allStories[currentIndex].title) {
            storyFullTitle.style.display = 'none';
        } else { 
            storyFullTitle.style.display = 'block';
            storyFullTitle.innerHTML = allStories[currentIndex].title;
        }
        clearInterval(timer);
        timer = setInterval(nextStory, 5000)
    }
});


