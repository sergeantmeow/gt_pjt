<!-- views/CreateView.vue -->

<template>
  <div class="container fw-bold">
    <h2 class="title-mg-ct">게시글 수정</h2>
    <form @submit.prevent="editArticle" class="row justify-content-center mt-4">
      <div class="col-md-6">
        <div class="form-group article-create">
          <label for="title">제목 : </label>
          <input type="text" id="title" v-model.trim="title" class="form-control"><br>
          <label for="content">내용 : </label>
          <textarea id="content" cols="50" rows="10" v-model="content" class="form-control"></textarea><br>
          <div v-if="image">
            <img :src="image" alt="이미지" class="article-img-create img-fluid">
          </div>
          <div class="form-group article-create">
            <label for="content">이미지 선택 : </label>
            <input type="file" id="image" ref="image" @change="handleImageChange"><br>
          </div>
          <div class="article-create submit-button">
            <input type="submit" id="submit" value="수정" class="btn btn-article-create fw-bold">
          </div>
        </div>
      </div>  
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleEditView',
  data() {
    return {
      title: '',
      content: '',
      image: '',
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created(){
    const { title, image, content } = this.$route.query;
    this.title = title;
    this.image = API_URL + image;
    this.content = content;
  },
  methods: {
    editArticle() {
      if (!this.title) {
        alert('제목 입력해주세요')
        return
      } else if (!this.content){
        alert('내용 입력해주세요')
        return
      }

      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('content', this.content);
      
      const headers = {
        Authorization: `Token ${this.$store.state.user.token}`,
      }

      if (this.$refs.image.files.length > 0) {
        headers['Content-Type'] = 'multipart/form-data';
        formData.append('image', this.$refs.image.files[0]);
      }

      axios({
        method: 'patch',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
        headers: headers,
        data: formData
      })
      .then(() => {
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },

    handleImageChange(event) {
      const file = event.target.files[0]
      const reader = new FileReader()

      reader.onload = (e) => {
        this.image = e.target.result
      }

      reader.readAsDataURL(file)
    },
  }
}
</script>

<style>

</style>
