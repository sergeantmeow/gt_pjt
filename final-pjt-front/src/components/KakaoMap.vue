<template>
  <div>
    <h2>TEST - KAKAOMAP 영화관들</h2>
    지역명으로 검색하기: <input type="text" placeholder="장소를 넣으세요" @keyup.enter="searchCinema">
    <button>
      <div @click="loadNearCinema">
        근처영화관 조회하기
      </div>
    </button>
    <div class="cinemas" v-for="rs in cinemaList" :key='rs.id' @click="showPlace(rs)" style="cursor: pointer">
      <h4>{{ rs.place_name }}</h4>
    </div>
    <div class="cinemas" v-for="rs in cinemaList" :key='rs.id' 
    @click="showPlace2(rs)" 
    style="cursor: pointer">
      <h4>{{ rs.name }}</h4>
    </div>
    <div class="kmap" ref="map">
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      cinemaList : null,
      options : {
        center: {
          lat: this.$store.state.userGEO[0],
          lng: this.$store.state.userGEO[1],
        },
        level: 4
      }
    }
  },
  mounted(){
    console.log(this.options.center)
    this.renderMap()
    this.nearbyCinema()
  },
  
  methods : {
    renderMap(){
      let kakao = window.kakao;
      const container = this.$refs.map
      // 33.450701, 126.570667
      const {center, level} = this.options
      const mapInstance = new kakao.maps.Map(container, {
        center: new kakao.maps.LatLng(center.lat, center.lng),
        level,
      }); 
      console.log(mapInstance)
    },

    nearbyCinema(){
      this.$store.dispatch('getCinemas')
    },

    loadNearCinema(){
      this.cinemaList = this.$store.state.cinemaList
    },

    searchCinema(e){
      const keyword = `${e.target.value} 영화관`
      const ps = new window.kakao.maps.services.Places()  
      ps.keywordSearch(keyword, (data, status, pgn)=>{
        console.log(data)
        console.log(status)
        console.log(pgn)
        this.cinemaList = data
      })
    },

    showPlace(place){
      this.options.center = {
        lat: place.y,
        lng: place.x,
      }
      this.options.level = 3
      this.renderMap()
    },

    showPlace2(){
      // this.options.center = {
      //   lat: place.cood_y,
      //   lng: place.cood_x,
      // }
      // this.options.level = 3
      // this.renderMap()
    },
  }
}
</script>

<style scoped>
  .kmap{
    width: 60%;
    height: 400px;
    margin: auto
  }
</style>