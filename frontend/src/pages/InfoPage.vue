<template>
    <div class="info">
        <div class="main__block">
        <navbar @entry="openEntry" @registration="openRegistration"></navbar>
        <dialog-window v-model:show="enterVisible">
          <enter-dialog></enter-dialog>
        </dialog-window>
        <dialog-window v-model:show="registrationVisible">
          <registration-dialog></registration-dialog>
        </dialog-window>
        <div class="about" id="about">
            <div class="about__background">
                <div class="about__inner">
                    <div class="about__image"/>

                    <div class="about__title">О нас</div>

                    <div class="about__content">
                        <div class="about__content_information">Мы организуем систему взаимодействия покупателей и производителей материалов</div>
                        <div class="about__content_btns">
                            <button class="about__content_btn">Узнать подробнее</button>
                        </div>

                    </div>
                </div>
            </div>
        
        </div>
        <div class="service" id="service">
            <div class="service__title">
                Для кого сервис?
            </div>
            <div class="service__item">
              <div class="service_item__customers">
                <div class="service_item__content">
                  <div class="service_item_content__title">
                    Для заказчиков стройматериалов
                  </div>
                  <div class="service_item_content__subtitle">
                    Строительные компании, стройбазы, магазины стройматериалов, дорожно-ремонтные компании
                  </div>
                  <a class="service_item_content__button" href="#customers">
                      <div class="service_item_content_button__text">Узнать подробнее</div>
                      <div class="service_item_content_button__arrow">➜</div>
                    </a>
              </div>
                </div>
                
              <div class="service_item__providers">
                <div class="service_item__content">
                    <div class="service_item_content__title">
                      Для поставщиков стройматериалов
                    </div>
                    <div class="service_item_content__subtitle">
                      Производители металлочерепицы, профнастила, фанеры, ОСБ-плит и т.п.
                    </div>
                    <a class="service_item_content__button" href="#providers">
                      <div class="service_item_content_button__text">Узнать подробнее</div>
                      <div class="service_item_content_button__arrow">➜</div>
                    </a>
                </div>
                
              </div>
            </div>
          </div>
        <div class="advantages">
          <div class="advantages__inner" id="customers">
            <div class="advantages_inner__title">Заказчикам</div>
            <div class="advantages_inner__element">
              <div class="advantages_inner_element__content">
                <img class="advantages_inner_element_content__icon" src="@/resources/images/leather_customers.svg"/>
                <div class="advantages_inner_element_content__title">Просто</div>
                <div class="advantages_inner_element_content__subtitle">Легкий способ найти нужного поставщика!</div>
              </div>
               <div class="advantages_inner_element__content">
                <img class="advantages_inner_element_content__icon" src="@/resources/images/price.svg"/>
                <div class="advantages_inner_element_content__title">Лучшие цены</div>
                <div class="advantages_inner_element_content__subtitle">За вашу заявку борятся десятки поставщиков, обеспечив минимальную цену!</div>
              </div>
               <div class="advantages_inner_element__content">
                <img class="advantages_inner_element_content__icon" src="@/resources/images/star.svg"/>
                <div class="advantages_inner_element_content__title">Лучшие партнеры</div>
                <div class="advantages_inner_element_content__subtitle">Рейтинг поставщика - выбирайте надежного партнера!</div>
              </div>
            </div>
          </div>
          <div class="advantages__inner" id="providers">
            <div class="advantages_inner__element">
              <div class="advantages_inner_element__content">
                <img class="advantages_inner_element_content__icon" src="@/resources/images/leather_providers.svg"/>
                <div class="advantages_inner_element_content__title">Просто</div>
                <div class="advantages_inner_element_content__subtitle">Легкий способ предложить свой товар заказчикам</div>
              </div>
               <div class="advantages_inner_element__content">
                <img class="advantages_inner_element_content__icon" src="@/resources/images/contacts.svg"/>
                <div class="advantages_inner_element_content__title">База заказчиков</div>
                <div class="advantages_inner_element_content__subtitle">Тысяча заказчиков вашей продукции</div>
              </div>
               <div class="advantages_inner_element__content">
                <img class="advantages_inner_element_content__icon" src="@/resources/images/clock.svg"/>
                <div class="advantages_inner_element_content__title">Работа в любое время</div>
                <div class="advantages_inner_element_content__subtitle">Работа с заявками в любомй момент</div>
              </div>
            </div>
            <div class="advantages_inner__title">Поставщикам</div>
          </div>
        </div>
        <div class="footer">
          <div class="footer__title">БСМ</div>
          <div class="footer__divider"></div>
        </div>
        </div>

    </div>
</template>

<script>
import Navbar from "@/components/InfoNavBar.vue"
import EnterDialog from '@/components/UI/EnterDialog.vue'
import RegistrationDialog from '@/components/UI/RegistrationDialog.vue'
    export default {
        components: {
            Navbar,
              EnterDialog,
              RegistrationDialog
        },
        data() {
          return {
            enterVisible: false,
            registrationVisible: false,
          }
        },
        methods: {
          openEntry(show){
            this.enterVisible = show;
          },
          openRegistration(show){
            this.registrationVisible = show;
          }
        },
    }
</script>

<style scoped>
.about {
  height: 500px;
  margin: 50px 0 0 0;
}
.about__background {
  background-image: url("@/resources/images/green_rectangle.svg");
  background-repeat: no-repeat;
  width: 100%;
  height: 100%;
    
}
.about__inner {
  display:flex;
  justify-content:space-between;
  height: 100%;
  max-width: 1440px;
  width: 100%;
  margin: 0 auto;
}
.about__image {
  background-image: url("@/resources/images/info_materials.svg");
  background-repeat: no-repeat;
  margin: auto 0;
  width: 500px;
  height: 370px;
}
.about__title {
  width: 440px;
  margin: 52.5px 0;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 60px;
  line-height: 73px;
  text-align: center;

  color: #FAF6ED;
}
.about__content {
  display: block;
  justify-content: center;
  margin: auto 0;
  align-items: center;
  width: 500px;
}
.about__content_information {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 30px;
  line-height: 36px;
  text-align: center;

  color: #FFFFFF;
}
.about__content_btns {
  width: 100%;
  margin-top: 33px;

}
.about__content_btn {
  margin: 0 25%;
  width: 263px;
  height: 46px;
  background: #FAF6ED;
  border-radius: 12px;
  border: 0;

  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 15px;
  line-height: 18px;
  text-align: center;
  color: #3F4155;
  transition-duration: 0.5s;
    
}
.about__content_btn:hover {
  color: #ffffff;
  background: #458686;
}
.service {
  cursor: default;
  width: 1440px;
  margin: 100px auto;
}
.service_item__customers {
  transition-duration: 0.5s;
}
.service_item__customers:hover {
  transform: translate(0, -10px);
}
.service_item__providers {
  transition-duration: 0.5s;
}
.service_item__providers:hover {
  transform: translate(0, -10px);
}
.service__title {
  text-align: center;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 60px;
  line-height: 73px;
  margin: 0 0 65px 0;
  text-align: center;

color: #3F4155;
}
.service_item_content__title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 30px;
  line-height: 36px;

  color: #FAF6ED;
}
.service__item {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  margin: 0 auto;
}
.service_item__customers {
  width: 490px;
  height: 280px;
  background: url("@/resources/images/background_customers.svg") no-repeat;
  border-radius: 20px;
  padding: 30px 25px;
}
.service_item__content {
  width: 63%;
}
.service_item__providers {
  width: 490px;
  height: 280px;
  background: url("@/resources/images/background_providers.svg") no-repeat;
  border-radius: 20px;
  padding: 30px 25px;
}
.service_item_content__subtitle {
  height: 83px;
  margin: 21px 0 0 0;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 22px;

  color: #FAF6ED;
}
.service_item_content__button {
  text-decoration: none;
  color: #FAF6ED;
  margin: 36px 0 0 0;
  display: flex;
  
}
.service_item_content__button:visited {
    color: #FAF6ED;
}
.advantages {
  display: block;
  height: 1000px;
  background: url("@/resources/images/info_triangles.svg") no-repeat;
}
.advantages__inner{
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  padding: 0 20px;
  width: 1440px;
  margin: 0 auto;
  height: 500px;
}
.advantages_inner__title {
  width: 25%;
  align-self: center;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 55px;
  line-height: 67px;
  text-align: left;
  color: #FAF6ED;
}
.advantages_inner__element {
  width: 75%;
  margin: 40px 0 0 0;
  display: flex;
  justify-content: space-between;

}
.advantages_inner_element__content {
  width: 30%;
}
.advantages_inner_element_content__icon {
  height: 93px;
  width: 100px;
}
.advantages_inner_element_content__title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 40px;
  line-height: 48px;

  color: #FAF6ED;
}
.advantages_inner_element_content__subtitle {
  margin: 10px 0 0 0;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 30px;
  line-height: 36px;

  color: #FAF6ED;
}
.footer {
  width: 1440px;
  margin: 0 auto;
  height: 100px;

}
.footer__title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 100px;

  color: #5CB25D;
}
.footer__divider {
    margin-top: 2px;
    height: 1px;
    background: gray;
}
</style>