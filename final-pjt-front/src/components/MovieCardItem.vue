<template>
  <div class="col">
    <router-link :to="{
      name: 'MovieDetailView',
      params: { id: movieItem.id }}">
      <div class="card">
        <img id="posterID" :src="`https://image.tmdb.org/t/p/w500/${movieItem.poster_path}`" class="card-img-top" alt="">
        <div class="card-body">
          <h4 class="card-title fw-bold">{{ movieItem?.title }}</h4>
          <!-- <p class="card-text card-description" id="overView">{{ movieItem?.overview }}</p> -->
          <p>평점 평균 : {{ movieItem?.vote_average }}</p>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieCardItem',
  props: {
    movieItem: Object,
  }
}
</script>

<style>
  #posterID {
    margin-left: 0px;
    margin-top: 0px;
  }
  
  .card-description {
  font-size: 15px;
  padding: 0 1rem;
   /* 추가하기 */
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical; 
  overflow: hidden;
}

.card-content__more-btn {
  appearance: none;
  border: 1px solid black;
  padding: 0.5em;
  border-radius: 0.25em;
  cursor: pointer;
  margin: 5px;
}

/* .card-content__more-btn::before {
  content: '더보기';
}

.card-content__more-btn:checked::before {
  content: '닫기';
}

.card-description:has(+ .card-content__more-btn:checked) {
  -webkit-line-clamp:unset
} */

</style>