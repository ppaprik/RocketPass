<template>
    <div>
      <!-- <h1>{{ pageData.title }}</h1>
       <h2>Products</h2> -->
      <p v-if="!isShopPage">{{ pageData.content }}</p>
      <ProductList v-if="isShopPage" />
    </div>
</template>
  

<script>
import pagesData from '../pages.json';
import ProductList from '../components/ProductList.vue';

export default {
  components: {
    ProductList
  },
  data() {
    return {
      pageData: {},
      isShopPage: false
    };
  },
  created() {
    this.loadPageData();
  },
  watch: {
    '$route'() {
      this.loadPageData();
    }
  },
  methods: {
    loadPageData() {
      const page = this.$route.name;
      this.pageData = pagesData[page] || { title: 'Page Not Found', content: 'Sorry, this page does not exist.' };
      this.isShopPage = page === 'shop';
    }
  }
};
</script>
  

<style scoped>
  /* div {
    
  } */

  h1 {
    font-size: 2rem;
    color: #333;
  }

  p {
    font-size: 1.2rem;
    color: #666;
  }
</style>
  