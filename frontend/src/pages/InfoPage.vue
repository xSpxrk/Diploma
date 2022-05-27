<template>
    <div class="info">
        <div class="main__block">
        <navbar></navbar>
        <div class="about">
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
        <div class="service">
            <div class="service__title">
                Для кого сервис?
            </div>
            <div class="service__item">
              <div class="service_item__customers">
                <div class="service_item__title">
                  Для заказчиков стройматериалов
                </div>
                <div class="service_item__subtitle">
                  Строительные компании, стройбазы, магазины стройматериалов, дорожно-ремонтные компании
                </div>
                <div class="service_item__button">
                  <div class="service_item_button__text">Узнать подробнее</div>
                  <div class="service_item_button__arrow">➜</div>
                </div>
              </div>
              <div class="service_item__providers">
                <div class="service_item__title">
                  Для поставщиков стройматериалов
                </div>
                <div class="service_item__subtitle">
                  Производители металлочерепицы, профнастила, фанеры, ОСБ-плит и т.п.
                </div>
                <div class="service_item__button">
                  <div class="service_item_button__text">Узнать подробнее</div>
                  <div class="service_item_button__arrow">➜</div>
                </div>
              </div>
            </div>
          </div>
        <div class="advantages">
          <div class="advantages_inner"></div>
          <div class="advantages_inner"></div>
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
    export default {
        components: {
            Navbar,
        }
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
  width: 1440px;
  margin: 100px auto;
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
.service_item__title {
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
.service_item__providers {
  width: 490px;
  height: 280px;
  background: url("@/resources/images/background_providers.svg") no-repeat;
  border-radius: 20px;
  padding: 30px 25px;
}
.service_item__button {
  display: flex;
  
}
.advantages {
  display: block;
  height: 1000px;
  background: url("@/resources/images/info_triangles.svg") no-repeat;
}
.advantages_inner{
  width: 1440px;
  margin: 0 auto;
  height: 500px;
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
  line-height: 121px;

  color: #5CB25D;
}
.footer__divider {
    margin-top: 2px;
    height: 1px;
    background: gray;
}
</style>