<template>
  <div class="container fw-bold login-color">
    <div class="row justify-content-center">
      <h2 class="title-mg-ct">{{ article?.title }}</h2>
      <div class="col-md-8">
        <div v-if="article && article.username" class="otheruser-link">
          <h4>
            <router-link :to="{ name: 'OtherProfileView', params: { username: article?.username } }">
              {{ article?.username }}
            </router-link>
          </h4>
        </div>
        <p>{{ formatDateTime(article?.created_at) }}</p>
        <div v-if="article && article.image" class="article-img-detail-container">
          <img :src="'http://127.0.0.1:8000' + article.image" alt="게시글 이미지" class="article-img-detail img-fluid">
        </div>
        <h5>{{ article?.content }}</h5>
        <div class="mt-2 mb-2">
          <span class="heart-icon" @click="likeArticle">
            <img src="@/assets/icon-heart.png" alt="좋아요 아이콘" class="article-icon-img">
          </span>
          <span class="fw-bold">
            {{ article?.like_users.length }}
          </span>
        </div>
        <div v-if="isAuthor" class="article-detail-btn">
          <span class="edit-icon" @click="editArticle">
            <img src="@/assets/icon-edit.png" alt="수정 아이콘" class="article-icon-img">
          </span>
          <span class="delete-icon" @click="deleteArticle">
            <img src="@/assets/icon-delete.png" alt="삭제 아이콘" class="article-icon-img">
          </span>
          <hr>
        </div>
        <ArticleComment :articleId="Number(articleId)" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleComment from '@/components/ArticleComment'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: null,
      articleId: '',
    }
  },
  components: {
    ArticleComment,
  },
  created() {
    this.articleId = this.$route.params.id
    this.getArticleDetail()
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    currentUser() {
      return this.$store.getters.currentUser
    },
    isAuthor() {
      return this.isLogin && this.article?.username === this.currentUser.username
    },
  },
  methods: {
    formatDateTime(dateTime) {
      if (!dateTime) return '';

      const date = new Date(dateTime);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');

      return `${year}-${month}-${day} ${hours}:${minutes}`;
    },
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/articles/${this.$route.params.id}/`,
      })
        .then((res) => {
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      },
    // 삭제하고 다른 페이지 이동 설정하기
    deleteArticle() {
      if (confirm('게시물을 삭제하시겠습니까?')) {
        axios({
          method: 'delete',
          url: `${API_URL}/articles/${this.$route.params.id}/delete/`,
          headers: {
          Authorization: `Token ${this.$store.state.user.token}`
          },
        })
          .then(() => {
            this.$router.push({ name: 'ArticleView' })
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    editArticle() {
      const params = {
        id: this.article.id,
        title: this.article.title,
        image: this.article.image,
        content: this.article.content
      }
      this.$router.push({ name: 'ArticleEditView', params: { id: this.article.id }, query: params })
    },
    likeArticle() {
      if(this.isLogin){
      axios({
        method: 'post',
        url: `${API_URL}/articles/${this.article.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`
        }
      })
        .then(() => {
          this.getArticleDetail()
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        alert('로그인한 유저만 좋아요를 할 수 있습니다.')
        this.$router.push('/login')
      }
    }
  }
}
</script>

<style>
.article-img-detail-container {
  margin-top: 10px;
  max-width: 100%;
  margin-bottom: 10px;
}

.article-img-detail {
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
}

.otheruser-link a {
  text-decoration: none;
  color: #bfbfbf
}

.otheruser-link a:hover {
  text-decoration: underline;
  color: #ff9ec3
}

.article-icon-img {
  width: 30px;
  height: 30px;
  transition: transform 0.2s ease-in-out;
  margin-left: 10px;
}

.article-icon-img:hover {
  transform: scale(1.3);
}

.article-detail-btn button {
  background-color: #7c6891;
  border-color: #7c6891;
  color: #bfbfbf;
}

.article-detail-btn button:hover {
  background-color: #7c6891;
  border-color: #7c6891;
  color: #ff2679;
}

.btn-article-view {
  background-color: #261639;
  color: #bfbfbf;
}

.btn-article-view:hover {
  background-color: #7c6891;
}
</style>
