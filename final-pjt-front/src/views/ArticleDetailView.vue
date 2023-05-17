<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="deleteArticle">삭제</button>
    <!-- 작성자일 경우만 삭제 가능하게 하기 -->
    <!-- 로그인했을 경우만 댓글 달 수 있게 하기 -->
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    getArticleDetail() {
      if (this.isLogin) {
        axios({
        method: 'get',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
        })
        .then((res) => {
          console.log(res)
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({name: 'LogInView'})
      }
    },
    // 삭제하고 다른 페이지 이동 설정하기
    deleteArticle(){ 
      axios({
        method: 'delete',
        url: `${API_URL}/articles/${ this.$route.params.id }/`
      })
      .then((res) => {
        console.log(res)
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>
