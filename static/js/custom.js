// back-to-top.js

window.onscroll = function () {
  const button = document.getElementById("back-to-top");
  if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    button.style.display = "block";
  } else {
    button.style.display = "none";
  }
};

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}

document.addEventListener("DOMContentLoaded", function () {
  // Функция для проверки, ведёт ли ссылка на изображение
  function isImageLink(url) {
    if (!url) return false;
    const imageExtensions = ["jpg", "jpeg", "png", "gif", "webp", "svg", "bmp", "ico"];
    try {
      const path = new URL(url, window.location.origin).pathname.toLowerCase();
      return imageExtensions.some((ext) => path.endsWith("." + ext));
    } catch (e) {
      return false;
    }
  }

  // Создаём элементы модального окна, если их ещё нет
  let modal = document.getElementById("imageModal");
  if (!modal) {
    modal = document.createElement("div");
    modal.id = "imageModal";
    modal.innerHTML = `
            <div class="modal-content">
                <img class="modal-image" id="modalImage" src="" alt="">
            </div>
            <span class="close">&times;</span>
        `;
    document.body.appendChild(modal);
  }

  const modalImage = document.getElementById("modalImage");
  const closeBtn = modal.querySelector(".close");

  // Ищем все ссылки на странице
  document.querySelectorAll("a[href]").forEach((link) => {
    if (isImageLink(link.href)) {
      link.addEventListener("click", function (event) {
        event.preventDefault(); // Отключаем переход по ссылке
        modalImage.src = this.href; // Устанавливаем src увеличенного изображения
        modal.style.display = "block"; // Показываем модальное окно
      });
    }
  });

  // Закрытие по крестику
  closeBtn.addEventListener("click", function () {
    modal.style.display = "none";
  });

  // Закрытие по клику на фон (но не по изображению и не по крестику)
  modal.addEventListener("click", function (event) {
    // Если клик был по самому изображению или по крестику – не закрываем
    if (event.target.classList.contains("modal-image") || event.target.classList.contains("close")) {
      return;
    }
    modal.style.display = "none";
  });

  // Закрытие по клавише Escape
  window.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && modal.style.display === "block") {
      modal.style.display = "none";
    }
  });
});
