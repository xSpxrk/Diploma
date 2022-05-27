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
                        <button class="about__content_btn">Узнать подробнее</button>
                    </div>
                </div>
            </div>
        
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
    margin-top: 50px;
}
.about__background {
    background-image: url("@/resources/info/green_rectangle.svg");
    background-repeat: no-repeat;
    width: 100%;
    height: 100%;
    
}
.about__inner {
    display:flex;
    justify-content:space-between;
    height: 100%;
    width: 1440px;
    margin: 0 auto;
}
.about__image {
    background-image: url("@/resources/info/info_materials.svg");
    background-repeat: no-repeat;
    margin: auto 0;
    width: 496px;
    height: 370px;
}
.about__title {
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
    width: 592px;
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
.about__content_btn {
    margin: 33px 0 0 30%;
    width: 263px;
    height: 46px;
    background: #FAF6ED;
    border-radius: 12px;
    color: #3F4155;
    border: 0;

    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 15px;
    line-height: 18px;

    text-align: center;

    color: #3F4155;
    

}
</style>